from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

#view for the index page
def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'ehealth_app/index.html', context_dict)

#view for the about page
def about(request):
    context_dict = {'content': "Some random string"}

    return render(request, 'ehealth_app/about.html', context_dict)