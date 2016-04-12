from django.contrib import admin

# Register your models here.
from .models import Series, Issue, Author, Publisher, SeriesGrouper, Trade, List

class SeriesAdmin(admin.ModelAdmin):
	list_display = ['name', 'publisher', 'seriesGrouper', 'updated', 'created']
	list_filter = ['current']

class IssueAdmin(admin.ModelAdmin):
	def series(self):
		return self.series.name
	series.admin_order_field = 'series__name'

	#fieldsets = [
	#	(None, {'fields': ['series', 'issue_number', 'variant']}),
	#	(None, {'fields': ['own', 'release_month', 'release_year']}),
	#	('If different from series', {'fields': ['author', 'publisher']}),
	#	]
	list_display = ['series', 'issue_number', 'cover_date', 'variant']
	list_filter = ['own']
	ordering = ('series__name', 'issue_number')

class TradeAdmin(admin.ModelAdmin):
	ordering = ('series__name', 'volume')
	
admin.site.register(Series, SeriesAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(SeriesGrouper)
admin.site.register(Trade, TradeAdmin)
#admin.site.register(List)

