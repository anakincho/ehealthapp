from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

#NOTE!!!! INSTALL DJANGO-REGISTRATION-REDUX v 1.2!!!! otherwise there is an error with get_success_url()

from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request,user):
        return '/ehealth_app/'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ehealth_app/', include('ehealth_app.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )