__author__ = 'Nikolay'
from django.conf.urls import patterns, url
from ehealth_app import views

#Defining the urls for our webApp
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name = 'about'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^profile/', views.profile, name = 'profile'),
		url(r'^tandc/', views.terms, name = 'tandc'),
		url(r'^category/(?P<category_name_slug>[\w\-]+)/edit/$', views.edit_category, name='edit_category'),
		url(r'^delete_category/(?P<category_name_slug>[\w\-]+)$', views.delete_category, name='delete_category'),
		url(r'^search/', views.search, name='search'),
        url(r'^api/search_autocomplete/', views.search_autocomplete, name='search_autocomplete'),
        )
