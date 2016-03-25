Set Up:

-clone https://github.com/anakincho/ehealthapp
-Launch cmd or your preferred console.
-Go onto a virtual environment.
-Navigate to correct directory "Workspace\ehealthapp\ehealth"
-type "pip install -r requirements.txt" as a command
-Run the population script using the command: "python populate_ehealth.py"
-Run the server using "python manage.py runserver"
-Go to "http://127.0.0.1:8000/ehealth_app/"
-Enjoy or detest our project.

After population script users available to login in with:
    username: jill password: jill
    username: joe password: joe
    username: jim password: jim

Project Specifications:

-A list of results will be returned from different sources. Pages from US website healthfinder.gov, MedlinePlus and other results from the world wide 
web should be returned. 

-The user can choose to see pages from a combination of these sources or just from a single
source.

-The page is analysed in many different ways. Readability. If the page gives of a happy or sad vibe. How likely the illness is.

-The user can create also create a profile.

-Once he/she has done so, they can create categories and add pages to them.

-The user can choose to make his created category or saved page private

-The user can edit or delete their created categories



Work Distribution:


Done by Niki -:
- Models (Categories, Pages) added all fields
- Made Categories, Pages sharable (a user can choose if a category/page is to be shared or no)
- Views
- Urls
- Some of the templates
- Forms
- Bootstrap beginning
- User profiles (a user can set up their profile, including profile pic and website, also important thing is that the implementation allows the user to edit his profile!)
- It is 2 a.m so I am not sure what else but I am sure I am missing half the stuff


- Implemented all the scores (flesh, subjectivity, polarity)
- Wrote down the pseudo code on how it should be implemented in the view
- fixed all the inline and internal css now is rewritten in an external file
- removed the internal js and rewrote it in external script.js file
- implemented the autocomplete feature with help from Carly for the suggestion list
- fixed some bugs and did some validation
- NOTE IMPORTANT ! team do pip install textstat and pip install textblob in your VE

- Implemented save pages functionality,
- fixed some major bugs
- fixed some html bugs
- wrote comments on views implemented

- implemented jquery validation on add category, add page,
- fixed styling on some of the templates (bootstrap was not added previously)
- removed some inline css
- fixed the healthfinder API not to break if there are no results or a bad keyword
- fixed medline API to work on pythonanywhere
- fixed population script, now working properly and populating the database as intended
- added new user to the population script and added extra fields for 'shared, user' on pages and categories
- fixed now add page and add category return to the homepage after submiting
- fixed other small bugs

Done by Carly -: 

Done by Calum -:
-Entire functionality for the search. Including what the user sees.
-The search template with the exception of pagination.
-Used the ratings methods for Readability, Polarity and Subjectivity to scan the content of the document getting the
 different scores
-Checkboxes to select API with accompanying javascript files.
-Population Script
-Restricted adding a page to logged in users
-Attempted add a page to category section but couldn't figure it out (Niki solved the problem)
-Moral support
 