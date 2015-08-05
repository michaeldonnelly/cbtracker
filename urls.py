from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views, forms

urlpatterns = [
	# Special pages
    url(r'^$', views.index, name='index'),
    url(r'^wantlist/$', login_required(views.Wantlist.as_view()), name='wantlist'),
    url(r'^picklist/$', login_required(views.Picklist.as_view()), name='picklist'),
    
    # Series
    url(r'^series/$', views.SeriesList.as_view(), name='series_list'),
	url(r'^series/(?P<series_id>\d+)/$', views.IssueList.as_view(), name='issues_by_series'),

	# Author
    url(r'^author/$', views.AuthorList.as_view(), name='author_list'),
	url(r'^author/(?P<author_id>\d+)/$', views.IssueList.as_view(), name='issues_by_author'),

	# Group
    url(r'^seriesGroup/$', views.SeriesGrouperList.as_view(), name='series_grouper_list'),
	url(r'^seriesGroup/(?P<seriesGrouper_id>\d+)/$', views.IssueList.as_view(), name='issues_by_group'),

#	url(r'^list/(?P<list_id>\d+)/$', views.IssueList.as_view(), name='list'),

	# Add issue
    url(r'^issue/add/$', views.issue, name='add_issue'),    

	# Edit issue
    url(r'^issue/(?P<issue_id>\d+)/$', views.issue, name='issue'),    
	url(r'^latestissue/(?P<series_id>\d+)/$', views.issue, name='latest_issue'),

    # Mark an issue as owned
    url(r'^issue/(?P<issue_id>\d+)/own/$', views.bought, name='own_issue'),    
	]