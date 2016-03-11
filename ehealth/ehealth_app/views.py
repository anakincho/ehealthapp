
#Imports of modules
from django.http import HttpResponse
from django.shortcuts import render
from ehealth_app.models import Category, Page

#view for the index page
def index(request):

    #fetching our categories from the database and ordering them by name
    #note we are fetching only 5 of them!
    category_list = Category.objects.order_by('name')[:5]

    #creating the context dictionary that we can use on our index template to show information for example from the DB
    context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict['categories'] = category_list

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'ehealth_app/index.html', context_dict)

#view for the about page
def about(request):
    context_dict = {'content': "Some random string"}

    return render(request, 'ehealth_app/about.html', context_dict)

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'ehealth_app/categories.html', context_dict)