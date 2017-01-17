from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from itertools import chain
import csv

from cbtracker.models import Issue, Series, SeriesGrouper, Author, List, Trade
from cbtracker.forms import IssueForm, TradeForm

def groupedBySeries(issues):
	series = []
	for i in issues:
		if not i.series.id in series:
			series.append(i.series.id)
	orderedSeries = Series.objects.filter(id__in=series).order_by('sort_name')
	all_issues_in_series = []
	for s in orderedSeries:
		issues_in_s = issues.filter(series = s)
		all_issues_in_series.append(issues_in_s)
	return all_issues_in_series
	
class Wantlist(ListView):
	model = Issue
	template = 'cbtracker/issue_list.html'
	current = True
	backissues = True
	
	def get(self, request, *args, **kwargs):
		include = request.GET.get('include')
		if include == 'current':
			self.backissues = False
		elif include == 'back':
			self.current = False
		response = super(Wantlist, self).get(request, *args, **kwargs)
		return response
	
	def get_context_data(self, **kwargs):
		context = super(Wantlist, self).get_context_data(**kwargs)
		context['title'] = 'Want List'
		context['wantlist'] = True
		context['includeSeriesName'] = True
		context['issues'] = Issue.objects.filter(own=False)

		if self.current:
			current_issue_ids = [issue.id for issue in Issue.objects.filter(own=False) if not issue.far_back()]
			context['current'] = Issue.objects.filter(id__in=current_issue_ids)

		if self.backissues:		
			#current_back_issue_ids = [issue.id for issue in Issue.objects.filter(own=False) if issue.current() and issue.far_back()]
			#old_issue_ids = [issue.id for issue in Issue.objects.filter(own=False) if not issue.current()]
			#historic_issue_ids = current_back_issue_ids + old_issue_ids
			historic_issue_ids = [issue.id for issue in Issue.objects.filter(own=False) if issue.far_back()]
			context['historic'] = Issue.objects.filter(id__in=historic_issue_ids).order_by('series', 'issue_number')
			context['grouped_by_series'] = groupedBySeries(context['historic'])
			
		return context
		
class Picklist(ListView):
	model = Series
	def get_context_data(self, **kwargs):
		context = super(Picklist, self).get_context_data(**kwargs)
		context['title'] = 'Current Series'
		marvel = Series.objects.filter(current=True, publisher=1)
		dc = Series.objects.filter(current=True, publisher__in=(3,4))
		indy = Series.objects.filter(current=True).exclude(publisher__in=(1,3,4))
		context['list'] = chain(indy, dc, marvel)
		context['picklist'] = True
		context['serieslist'] = True
		return context
		
class Pulllist(ListView):
	model = Series
	def get_context_data(self, **kwargs):
		context = super(Pulllist, self).get_context_data(**kwargs)
		context['title'] = 'Pull List'
		context['list'] = Series.objects.filter(
			Q(current = True) &
			(
			Q(pullList = True) |
			Q(seriesGrouper__pullList = True) |
			Q(author__pullList = True) 
			))			
		context['authors'] = Author.objects.filter(pullList = True)
		context['seriesGroupers'] = SeriesGrouper.objects.filter(pullList = True)
		context['pulllist'] = True
		context['serieslist'] = True
		return context
	
	
	
# All Series
class SeriesList(ListView):
	model = Series
	def get_context_data(self, **kwargs):
		context = super(SeriesList, self).get_context_data(**kwargs)
		context['title'] = 'Series'
		context['list'] = Series.objects.all()
		context['serieslist'] = True
		return context	
		
class SeriesGrouperList(ListView):
	model = SeriesGrouper
	def get_context_data(self, **kwargs):
		context = super(SeriesGrouperList, self).get_context_data(**kwargs)
		context['title'] = 'Series Groupers'
		context['list'] = SeriesGrouper.objects.all()
		context['seriesgrouplist'] = True
		return context	
	
class AuthorList(ListView):
	model = Author
	def get_context_data(self, **kwargs):
		context = super(AuthorList, self).get_context_data(**kwargs)
		context['title'] = 'Authors'
		context['list'] = Author.objects.all()
		context['authorlist'] = True
		return context		

class IssueList(ListView):
	model = Issue
	def get_context_data(self, **kwargs):
		context = super(IssueList, self).get_context_data(**kwargs)
		context['wantlist'] = False
		context['includeSeriesName'] = False
		
		# Series Group
		try:
			seriesGrouper_id = self.kwargs['seriesGrouper_id']
			seriesGrouper = SeriesGrouper.objects.get(pk = seriesGrouper_id)
			context['historic'] = Issue.objects.filter(series__seriesGrouper = seriesGrouper).order_by('cover_year', 'cover_month')
			context['includeSeriesName'] = True
			context['title'] = seriesGrouper		
			return context
		except KeyError:
			pass
			
		# Author
		try:
			author_id = self.kwargs['author_id']
			author = Author.objects.get(pk = author_id)
			context['historic'] = Issue.objects.filter(Q(series__author = author) & Q(author = None)| Q(author = author)).order_by('cover_year', 'cover_month', 'series__name')
			context['includeSeriesName'] = True
			context['title'] = author	
			context['includePublisher'] = True
			context['addIssueQueryParams'] = 'author=' + author_id
			context['grouped_by_series'] = groupedBySeries(context['historic'])
			return context
		except KeyError:
			pass
			
		# Series
		series_id = self.kwargs['series_id']
		series = Series.objects.get(id=series_id)
		context['series'] = series
		context['title'] = series
		context['historic'] = Issue.objects.filter(series = series_id).order_by('issue_number')
		context['addIssueQueryParams'] = 'series=' + series_id
		return context

class TradeList(ListView):
	model = Trade
	def get_context_data(self, **kwargs):
		context = super(TradeList, self).get_context_data(**kwargs)
		context['title'] = 'Trades'
		context['list'] = Trade.objects.all()
		context['tradelist'] = True
		return context
		
@login_required
def issue(request, issue_id='', series_id='', author_id='', list_id='', return_to=''):
	if request.method == 'POST':
		if issue_id:
			update_issue = Issue.objects.get(pk=issue_id)
			form = IssueForm(request.POST, instance=update_issue)
		else:
			form = IssueForm(request.POST)
		
		if form.is_valid():
			form.save()
			url = form.cleaned_data['referrer']
			if url == '':
				url = '/cbtracker'
			return HttpResponseRedirect(url)			
		# TODO: what if the form isn't valid?
		else:
			return HttpResponse('Failed to save issue')
	
	
	# If this is the latestissue URL, find the last issue for the series provided
	if request.path_info.split('/')[2] == 'latestissue':
		issue_id = Series.objects.get(pk=series_id).latest_issue().id	

	# Prep form with default values	
	context = RequestContext(request)
	referrer = None
	try:
		referrer = request.META['HTTP_REFERER']
	except KeyError:
		pass

	# Updating an existing issue
	if issue_id:
		update_issue = Issue.objects.get(pk=issue_id)
		form = IssueForm(instance = update_issue, initial={'referrer': referrer})
		context['title'] = 'Update ' + str(update_issue)
		
	# Creating a new issue
	else:
		series = None
		issue_number = None
		cover_month = None
		cover_year = None
		story_name = None
		story_part = None
		author = None
		fair_price = None
		price_source = None
		
		author_id = request.GET.get('author')
		series_id = request.GET.get('series')
		
		context['title'] = 'Add Comic'
		if series_id:
			own = False
			series = Series.objects.get(pk=series_id)
			latest_issue = series.latest_issue()
			if latest_issue:
				issue_number = latest_issue.issue_number + 1
				#own = latest_issue.own
				if latest_issue.cover_month < 12:
					cover_year = latest_issue.cover_year
					cover_month = latest_issue.cover_month + 1
				else:
					cover_year = latest_issue.cover_year + 1
					cover_month = 1
				if latest_issue.story_part:
					story_name = latest_issue.story_name
					story_part = latest_issue.story_part + 1
				author = latest_issue.author
				fair_price = latest_issue.fair_price
				price_source = latest_issue.price_source
			else:
				issue_number = 1
				cover_year = series.start_year
			context['title'] = context['title'] + ' - ' + str(series)
		else:
			own = False
		if author_id:
			author = Author.objects.get(pk=author_id)
		form = IssueForm(initial={
			'series': series, 
			'own': own, 
			'issue_number': issue_number,
			'cover_year': cover_year,
			'cover_month': cover_month,
			'story_name': story_name,
			'story_part': story_part,
			'fair_price': fair_price,
			'price_source': price_source,
			'author': author,
			'referrer': referrer
		})
	# endif
	
	return render(request, 'cbtracker/issue_form.html', {'form': form,}, context)

@login_required
def trade(request, trade_id=''):
	if request.method == 'POST':
		if trade_id:
			update_trade = Trade.objects.get(pk=trade_id)
			form = TradeForm(request.POST, instance=update_trade)
		else:
			form = TradeForm(request.POST)
		
		if form.is_valid():
			form.save()
			url = form.cleaned_data['referrer']
			if url == '':
				url = '/cbtracker'
			return HttpResponseRedirect(url)			
		# TODO: what if the form isn't valid?
		else:
			return HttpResponse('Failed to save trade')
	
	# Prep form with default values	
	context = RequestContext(request)
	referrer = None
	try:
		referrer = request.META['HTTP_REFERER']
	except KeyError:
		pass

	# Updating an existing issue
	if trade_id:
		update_trade = Trade.objects.get(pk=trade_id)
		form = TradeForm(instance = update_trade, initial={'referrer': referrer})
		context['title'] = 'Update ' + str(update_trade)
		
	# Creating a new issue
	else:
		series = None
		volume = None
		own = True
		context['title'] = 'Add Trade'
		form = TradeForm(initial={
			'series': series, 
			'own': own, 
			'volume': volume,
			'referrer': referrer
		})
	# endif
	
	return render(request, 'cbtracker/trade_form.html', {'form': form,}, context)

@login_required
def latestIssue(request, series_id):
	series = Series.objects.get(pk=series_id)
	issue = series.latest_issue()

	return issue(request, issue.id)
	#return HttpResponse(issue.id)

@login_required
def bought(request, issue_id):
	try:
		issue = Issue.objects.get(pk=issue_id)
		issue.own = True
		if issue.release_month == '':
			issue.release_month = issue.cover_month
		if issue.release_year == '':
			issue.release_year = issue.cover_year
		issue.save()
		return HttpResponse('bought' + issue_id)
	except:
		return HttpResponse('error')

@login_required		
def index(request):
	return HttpResponseRedirect('wantlist')		
    #return HttpResponse("Hello, world. You're at the comicbook index.")
