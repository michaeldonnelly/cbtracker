from django.db import models
import datetime

class Series(models.Model):
	name = models.CharField(max_length=200)
	sort_name = models.CharField(max_length=200)
	author = models.ForeignKey('Author', null=True, blank=True)
	volume = models.IntegerField(null=True, blank=True)
	publisher = models.ForeignKey('Publisher', null=True, blank=True)
	start_year = models.IntegerField()
	current = models.BooleanField(default=False)
	pullList = models.BooleanField(default=False)
	seriesGrouper = models.ForeignKey('SeriesGrouper', null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	#finalIssue = models.IntegerField(null=True, blank=True)

	def latest_issue(self):
		return Issue.objects.filter(series=self).first()
	
	class Meta:
		verbose_name_plural = 'series'
		ordering = ['sort_name', 'start_year']
		
	def __str__(self):
		return self.name + ' (' + str(self.start_year) + ')'


	def remove_article(name):
		splitName = name.split(' ',1)
		if splitName[1].lower == 'the':
			return splitName[2]
		return name	
		
	def save(self, *args, **kwargs):
		#self.sort_name = self.remove_article(self.name)
		super(Series, self).save(*args, **kwargs)	
		
class SeriesGrouper(models.Model):
	name = models.CharField(max_length=200)
	pullList = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['name']
	
	def __str__(self):
		return self.name
	
def date_ym(year, month):
	try:
		date = str(year) + '-' 
		if month < 10:
			date = date + '0'
		date = date + str(month)
		return date		
	except TypeError:
		return ""
	
def date_ymd(year, month, day):
	date = date_ym(year, month)

	if day == 0:
		return date

	date = date + '-'
	if day < 10:
		date = date + '0'
	date = date + str(day)
	return date

class Issue(models.Model):
	series = models.ForeignKey('Series')
	issue_number = models.IntegerField()
	own = models.BooleanField(default=False)
	want = models.BooleanField(default=True)
	ordered = models.BooleanField(default=False)
	release_day = models.IntegerField(default=0, null=False, blank=False)
	release_month = models.IntegerField(null=True, blank=True)
	release_year = models.IntegerField(null=True, blank=True)
	cover_month = models.IntegerField(null=True, blank=True)
	cover_year = models.IntegerField(null=True, blank=True)
	variant = models.CharField(max_length=100, blank=True)
	story_name = models.CharField(max_length=100, blank=True)
	story_part = models.IntegerField(null=True, blank=True)
	author = models.ForeignKey('Author', null=True, blank=True)
	publisher = models.ForeignKey('Publisher', null=True, blank=True)
	fair_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	price_source = models.CharField(max_length=100, blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def current(self):
		return self.series.current
		
	def issue_author(self):
		if author:
			return author
		return series.author
		
	def cover_date(self):
		return date_ym(self.cover_year, self.cover_month)
		
	def cover_date_with_day(self):
		return date_ymd(self.cover_year, self.cover_month, self.cover_day)
		
	def release_date(self):
		return date_ym(self.release_year, self.release_month)
		
	def release_date_with_day(self):
		return date_ymd(self.release_year, self.release_month, self.release_day)
		
	def release_delta(self):
		try:
			year = self.release_year
			month = self.release_month
			day = self.release_day
			if year < 1:
				year = self.cover_year
				month = self.cover_month
			if month < 1:
				month = 1
			if day < 1:
				day = 1
			release = datetime.date(year, month, day)
		except TypeError:
			release = datetime.date.today()		
		delta = release - datetime.date.today()
		return delta		
		
	def far_out(self):
		return self.release_delta() > datetime.timedelta(days = 0)

	def far_back(self):
		return self.release_delta() < datetime.timedelta(days = -90)	

	class Meta:
		ordering = ['-cover_year', '-cover_month', '-issue_number']

	def __str__(self):
		return self.series.name + ' #' + str(self.issue_number) + ' ' + self.variant

class Author(models.Model):
	name = models.CharField(max_length=200)
	pullList = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['name']
		
	def __str__(self):
		return self.name 
	
class Publisher(models.Model):
	name = models.CharField(max_length=100)
	imprint_of = models.ForeignKey('self', null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['name']
		
	def __str__(self):
		pub = self.name
		if self.imprint_of != None:
			pub = pub + ' (' + self.imprint_of.name + ')'
		return pub 
		
class Trade(models.Model):
	series = models.ForeignKey('Series')
	volume = models.IntegerField()
	own = models.BooleanField(default='true')
	title = models.CharField(max_length=200, null=True, blank=True)
	BINDING_CHOICES = (
		(0, 'Paperback'),
		(1, 'Hardcover'),
	)
	binding = models.IntegerField(choices = BINDING_CHOICES, default=0) 
	release_month = models.IntegerField(null=True, blank=True)
	release_year = models.IntegerField(null=True, blank=True)
	
	def release_date(self):
		return date_ym(self.release_year, self.release_month)

	def release_delta(self):
		try:
			day = 1
			release = datetime.date(self.release_year, self.release_month, day)
		except TypeError:
			release = datetime.date.today()		
		delta = release - datetime.date.today()
		return delta		

	def unreleased(self):
		return self.release_delta() > datetime.timedelta(days = 0)
		
	class Meta:
		ordering = ['series', 'volume']

	def __str__(self):
		trade = self.series.name + ' #' + str(self.volume)
		if self.title != None:
			trade = trade + ' - ' + self.title
		return trade
	
	
class List(models.Model):
	name = models.CharField(max_length=200)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	series = models.ManyToManyField(Series, blank=True)
	issues = models.ManyToManyField(Issue, blank=True)

	def __str__(self):
		return self.name 

# this was needed for some migrations		
def made():
	return datetime.datetime(2015,7,10,16,24)

