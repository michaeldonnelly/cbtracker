from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.template import RequestContext
from django.db.models import Q
from itertools import chain

from comicbooks.models import Issue, Series, SeriesGrouper, Author, List
from comicbooks.forms import IssueForm

class Wantlist(ListView):
	model = Issue
	template = 'comicbooks/issue_list.html'
	
	def get_context_data(self, **kwargs):
		context = super(Wantlist, self).get_context_data(**kwargs)
		context['title'] = 'Want List'
		context['wantlist'] = True
		context['includeSeriesName'] = True
		context['issues'] = Issue.objects.filter(own=False)
		
		current_issue_ids = [issue.id for issue in Issue.objects.filter(own=False) if issue.current()]
		context['current'] = Issue.objects.filter(id__in=current_issue_ids)
		
		historic_issue_ids = [issue.id for issue in Issue.objects.filter(own=False) if not issue.current()]
		context['historic'] = Issue.objects.filter(id__in=historic_issue_ids).order_by('series', 'issue_number')

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
			context['historic'] = Issue.objects.filter(series__seriesGrouper = seriesGrouper).order_by('release_year', 'release_month', 'release_day')
			context['includeSeriesName'] = True
			context['title'] = seriesGrouper		
			return context
		except KeyError:
			pass
			
		# Author
		try:
			author_id = self.kwargs['author_id']
			author = Author.objects.get(pk = author_id)
			context['historic'] = Issue.objects.filter(Q(series__author = author) | Q(author = author)).order_by('release_year', 'release_month', 'release_day', 'series__name')
			context['includeSeriesName'] = True
			context['title'] = author		
			return context
		except KeyError:
			pass
			
		# List
		try:
			list_id = self.kwargs['list_id']
			list = List.objects.get(pk = list_id)
			
			#marvelS = list.series.filter(publisher__in = (1,5))
			#dcS = list.series.filter(publisher__in = (3,4))
			#indyS = list.series.exclude(publisher__in = (1,3,4,5))
			
			#marvelI = Issue.objects.filter(own = False, series__in = marvelS)
			#dcI = Issue.objects.filter(own = False, series__in = dcS)
			#indyI = Issue.objects.filter(own = False, series__in = indyS)
			
			
			seriesList = list.series.all()
			issueList = Issue.objects.filter(own = False, series__in=seriesList)
			context['historic'] = issueList.order_by('series__name')
			
			
			#seriesList = list.series.all()
			#context['historic'] = Issue.objects.filter(own = False, series__in=seriesList)
			
			#context['historic'] = chain(marvelI, dcI, indyI)
			context['includeSeriesName'] = True
			context['title'] = list
			#context['title'] = seriesList
			context['wantlist'] = True
			return context
		except KeyError:
			pass
			

		series_id = self.kwargs['series_id']
		series = Series.objects.get(id=series_id)
		context['series'] = series
		context['title'] = series
		context['historic'] = Issue.objects.filter(series = series_id).order_by('issue_number')
		return context

class Picklist(ListView):
	model = Series
	def get_context_data(self, **kwargs):
		context = super(Picklist, self).get_context_data(**kwargs)
		context['title'] = 'Current Series'
		marvel = Series.objects.filter(current=True, publisher=1)
		dc = Series.objects.filter(current=True, publisher__in=(3,4))
		indy = Series.objects.filter(current=True).exclude(publisher__in=(1,3,4))
		#context['list'] = Series.objects.filter(current=True).order_by('publisher','name')
		context['list'] = chain(indy, dc, marvel)
		return context
	
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
	
def issue_form_upload(request):
	if request.method == 'GET':
	    #return HttpResponse("Foo")
	    form = IssueForm()
	else:
		# A POST request: Handle Form Upload
		# Bind data from request.POST into a PostForm
		form = IssueForm(request.POST)
		# If data is valid, proceeds to create a new post and redirect the user
		if form.is_valid():
			issue = form.save()
			return HttpResponseRedirect('series/' + str(issue.series.id))
	return render(request, 'comicbooks/issue_form_upload.html', {
		'form': form,
	})

def issue(request, issue_id='', series_id='', author_id='', list_id=''):
	if request.method == 'POST':
		if issue_id:
			update_issue = Issue.objects.get(pk=issue_id)
			form = IssueForm(request.POST, instance=update_issue)
		else:
			form = IssueForm(request.POST)
		if form.is_valid():
			form.save()
			url = '/comics/'
			if series_id:
				url = url + 'series/' + series_id
			if author_id:
				url = url + 'author/' + author_id
			url = '../..'
			return HttpResponseRedirect(url)			
		# TODO: what if the form isn't valid?

	# Prep form with default values	
	context = RequestContext(request)
	series = None
	issue_number = None
	release_month = None
	release_year = None
	story_name = None
	story_part = None
	author = None
	fair_price = None
	price_source = None
	
	if issue_id:
		update_issue = Issue.objects.get(pk=issue_id)
		form = IssueForm(instance = update_issue)
		context['title'] = 'Update ' + str(update_issue)
	else:
		context['title'] = 'Add Comic'
		if series_id:
			own = True
			series = Series.objects.get(pk=series_id)
			latest_issue = series.latest_issue()
			if latest_issue:
				issue_number = latest_issue.issue_number + 1
				own = latest_issue.own
				if latest_issue.release_month < 12:
					release_year = latest_issue.release_year
					release_month = latest_issue.release_month + 1
				else:
					release_year = latest_issue.release_year + 1
					release_month = 1
				if latest_issue.story_part:
					story_name = latest_issue.story_name
					story_part = latest_issue.story_part + 1
				author = latest_issue.author
				fair_price = latest_issue.fair_price
				price_source = latest_issue.price_source
			else:
				issue_number = 1
				release_year = series.start_year
			context['title'] = context['title'] + ' - ' + str(series)
		else:
			own = False
		if author_id:
			author = Author.objects.get(pk=author_id)
		form = IssueForm(initial={
			'series': series, 
			'own': own, 
			'issue_number': issue_number,
			'release_year': release_year,
			'release_month': release_month,
			'story_name': story_name,
			'story_part': story_part,
			'fair_price': fair_price,
			'price_source': price_source,
			'author': author,
		})
	return render(request, 'comicbooks/issue_form.html', {'form': form,}, context)

def issueOwn(request, issue_id):
	issue = Issue.objects.get(pk=issue_id)
	issue.own = True
	issue.save()
	try:
		return HttpResponseRedirect(request.META['HTTP_REFERER'])
	except KeyError:
		return HttpResponseRedirect('/comics/')		

def bought(request, issue_id):
	try:
		issue = Issue.objects.get(pk=issue_id)
		issue.own = True
		issue.save()
		return HttpResponse('bought' + issue_id)
	except:
		return HttpResponse('error')
	
	
def index(request):
    return HttpResponse("Hello, world. You're at the comicbook index.")
    
def wantlist(request):
	return "foo"
	
