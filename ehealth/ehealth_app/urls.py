__author__ = 'Nikolay'
from django.conf.urls import patterns, url
from ehealth_app import views

#Defining the urls for our webApp
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name = 'about'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        )