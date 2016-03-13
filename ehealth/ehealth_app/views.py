
#Imports of modules
from django.http import HttpResponse
from django.shortcuts import render
from ehealth_app.models import Category, Page
from ehealth_app.forms import CategoryForm
from datetime import datetime

#view for the index page
def index(request):

    #fetching our categories from the database and ordering them by name
    #note we are fetching only 5 of them!
    category_list = Category.objects.order_by('name')[:5]

    #creating the context dictionary that we can use on our index template to show information for example from the DB
    context_dict = {'boldmessage': "I am bold font from the context"}
    context_dict['categories'] = category_list

    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).seconds > 0:
            # ...reassign the value of the cookie to +1 of what it was before...
            visits = visits + 1
            # ...and update the last visit cookie, too.
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    context_dict['visits'] = visits


    response = render(request,'ehealth_app/index.html', context_dict)

    return response

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.


#view for the about page
def about(request):
    context_dict = {'content': "Some random string"}
    if request.session.get('visits'):
        count = request.session.get('visits')
    else:
        count = 0

# remember to include the visit data
    return render(request, 'ehealth_app/about.html', {'visits': count})

    #return render(request, 'ehealth_app/about.html', context_dict)

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



def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Render the form with error messages (if any).
    return render(request, 'ehealth_app/add_category.html', {'form': form})