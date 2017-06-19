from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Series, Issue, Author, Publisher, Tag, SeriesGrouper, Trade, List

# Admin drop down functions
def make_not_current(modeladmin, request, queryset):
	queryset.update(current=False)
	queryset.update(pullList=False)	# If it isn't current, don't pull it
make_not_current.short_description = "Set selected series as no longer current"

def remove_from_pulllist(modeladmin, request, queryset):
	queryset.update(pullList=False)
remove_from_pulllist.short_description = "Remove from pull list"

def add_to_pulllist(modeladmin, request, queryset):
	queryset.update(pullList=True)
add_to_pulllist.short_description = "Add to pull list"

def tag_xmen(modeladmin, request, queryset):
	xmen = Tag.objects.get(name="X-Men")
	for series in queryset:
		series.tags.add(xmen)		
tag_xmen.short_description = "Tag as X-Men"

def ordered(modeladmin, request, queryset):
	queryset.update(ordered=True)
ordered.short_description = "Ordered"

def wanted(modeladmin, request, queryset):
	queryset.update(want=True)
wanted.short_description = "Wanted"

def not_wanted(modeladmin, request, queryset):
	queryset.update(want=False)
not_wanted.short_description = "Not Wanted"

# Admin Screens
class SeriesAdmin(admin.ModelAdmin):
	list_display = ['name', 'publisher', 'seriesGrouper', 'updated', 'created']
	list_filter = ['current', 'pullList', 'publisher', 'tags']
	actions = [add_to_pulllist, remove_from_pulllist, make_not_current, tag_xmen]

class IssueResource(resources.ModelResource):
	class Meta:
		model = Issue
		skip_unchanged = True
		report_skipped = False

#class IssueAdmin(admin.ModelAdmin):
class IssueAdmin(ImportExportModelAdmin):
	def series(self):
		return self.series.name
	series.admin_order_field = 'series__name'

	#fieldsets = [
	#	(None, {'fields': ['series', 'issue_number', 'variant']}),
	#	(None, {'fields': ['own', 'release_month', 'release_year']}),
	#	('If different from series', {'fields': ['author', 'publisher']}),
	#	]
	list_display = ['series', 'issue_number', 'cover_date', 'variant', 'fair_price', 'story_name']
	list_filter = ['own', 'want', 'ordered', 'pullList']
	ordering = ('series__name', 'issue_number')
	resource_class = IssueResource
	actions = [ordered, add_to_pulllist, wanted, not_wanted, tag_xmen]


class TradeAdmin(admin.ModelAdmin):
	ordering = ('series__name', 'volume')

class PullableAdmin(admin.ModelAdmin):
	list_filter = ['pullList']
	actions = [add_to_pulllist, remove_from_pulllist]
	
	
admin.site.register(Series, SeriesAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Author, PullableAdmin)
admin.site.register(Tag)
admin.site.register(Publisher)
admin.site.register(SeriesGrouper, PullableAdmin)
admin.site.register(Trade, TradeAdmin)
#admin.site.register(List)

