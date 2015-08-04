from django.conf.urls import url

from . import views, forms
#from comicbooks.views import IssueListView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wantlist/$', views.Wantlist.as_view(), name='wantlist'),
    url(r'^picklist/$', views.Picklist.as_view(), name='picklist'),
    url(r'^series/$', views.SeriesList.as_view(), name='series_list'),
	url(r'^series/(?P<series_id>\d+)/$', views.IssueList.as_view(), name='issues_by_series'),
    url(r'^seriesGroup/$', views.SeriesGrouperList.as_view(), name='series_grouper_list'),
	url(r'^seriesGroup/(?P<seriesGrouper_id>\d+)/$', views.IssueList.as_view(), name='issues_by_group'),
    url(r'^author/$', views.AuthorList.as_view(), name='author_list'),
	url(r'^author/(?P<author_id>\d+)/$', views.IssueList.as_view(), name='issues_by_author'),
	url(r'^author/(?P<author_id>\d+)/issue/add/$', views.issue, name='add_issue'),
    url(r'^issue_form_upload.html$', views.issue_form_upload, name='issue_form_upload'),
    #url(r'^issue/form_upload.html$', forms.IssueForm.as_table(), name='issue_form_upload'),
    #url(r'^issue/form_upload.html$', forms.IssueForm, name='issue_form_upload'),
    url(r'^issue/add/$', views.issue, name='issue'),    
    url(r'^issue/(?P<issue_id>\d+)/$', views.issue, name='issue'),    
    #url(r'^issue/(?P<issue_id>\d+)/own/$', views.issueOwn, name='own_issue'),    
    url(r'^issue/(?P<issue_id>\d+)/own/$', views.bought, name='own_issue'),    
	url(r'^series/(?P<series_id>\d+)/issue/add/$', views.issue, name='issue'),
	url(r'^series/(?P<series_id>\d+)/issue/(?P<issue_id>\d+)/$', views.issue, name='issue'),
	url(r'^wantlist/issue/add/$', views.issue, name='issue'),
	url(r'^wantlist/issue/(?P<issue_id>\d+)/$', views.issue, name='issue'),
	url(r'^picklist/issue/add/$', views.issue, name='add_issue'),
	url(r'^series/issue/add/$', views.issue, name='add_issue'),
	url(r'^seriesGroup/issue/add/$', views.issue, name='add_issue'),
	url(r'^author/issue/add/$', views.issue, name='add_issue'),
	url(r'^list/(?P<list_id>\d+)/$', views.IssueList.as_view(), name='list'),
	url(r'^list/(?P<list_id>\d+)/issue/(?P<issue_id>\d+)/$', views.issue, name='issue'),
]