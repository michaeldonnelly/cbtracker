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
	seriesGrouper = models.ForeignKey('SeriesGrouper', null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
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
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['name']
	
	def __str__(self):
		return self.name
	
class Issue(models.Model):
	series = models.ForeignKey('Series')
	issue_number = models.IntegerField()
	own = models.BooleanField(default='true')
	release_day = models.IntegerField(default=0, null=False, blank=False)
	release_month = models.IntegerField()
	release_year = models.IntegerField()
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
		
	def release_date(self):
		date = str(self.release_year) + '-' 
		if self.release_month < 10:
			date = date + '0'
		date = date + str(self.release_month)
		return date		
		
	def release_date_with_day(self):
		date = self.release_date()

		if self.release_day == 0:
			return date

		date = date + '-'
		if self.release_day < 10:
			date = date + '0'
		date = date + str(self.release_day)
		return date
		
	def release_delta(self):
		day = self.release_day
		if day < 1:
			day = 1
		release = datetime.date(self.release_year, self.release_month, day)
		delta = release - datetime.date.today()
		return delta		
		
	def far_out(self):
		return self.release_delta() > datetime.timedelta(days = 13)

	def far_back(self):
		return self.release_delta() < datetime.timedelta(days = 90)	

	class Meta:
		ordering = ['-release_year', '-release_month', '-release_day', '-issue_number']

	def __str__(self):
		return self.series.name + ' #' + str(self.issue_number) + ' ' + self.variant

class Author(models.Model):
	name = models.CharField(max_length=200)
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

