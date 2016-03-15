
#Imports of modules
from django.http import HttpResponse
from django.shortcuts import render
from ehealth_app.models import Category, Page, UserProfile
from ehealth_app.forms import CategoryForm, UserProfileForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

#view for the index page
def index(request):

    #fetching our categories from the database and ordering them by name

    category_list = Category.objects.order_by('name')

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

    # Get the username of the currently logged user
    # in order to return the appropriate pages for the requested category
    if request.user.is_authenticated():
        username = request.user.username

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)


        newPages = []
        # if the user has no saved pages, and there are not any shared pages for the given category,
        # this will help us return 0 pages(easier to implement in the template when no pages are returned)
        # otherwise this will return the pages either saved by the user or all the shared pages for this category
        for page in pages:
            if page.shared:
                newPages.append(page)
            elif page.user == username:
                newPages.append(page)


        # Adding our filtered pages to the context dictionary
        context_dict['pages'] = newPages

        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
        print category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'ehealth_app/categories.html', context_dict)



def add_category(request):

    # In order to record which user has created the category!
    if request.user.is_authenticated():
        username = request.user.username

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            note = form.save(commit=True)
            print note.name
            note.user = username
            # Save the new category to the database.
            note.save()

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

@login_required
def profile(request):

    # Get the username of the currently logged in user
    if request.user.is_authenticated():
        user = request.user

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if profile_form.is_valid():

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            if UserProfile.objects.filter(user=user).count() == 0: # if no userProfile exists, we create one
                profile = profile_form.save(commit=False)
                profile.user = user
            else: # otherwise we fetch the existing one and alter its fields
                profile = UserProfile.objects.get(user=user)

            profile.website = request.POST['website']

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()
            
            return index(request)

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'ehealth_app/profile.html',
            {'profile_form': profile_form} )