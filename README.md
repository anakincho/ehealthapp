"# ehealthapp"

For Tutors, Lecturer if you are reading this, please reffer to the readme.txt file inside the ehealth
folder above. The specifications and work distribution are described there, this file
was initially used by team members, the official readme.txt is found in: https://github.com/anakincho/ehealthapp/blob/master/ehealth/readme.txt

IMPORTANT NOTE!!!! when installing requirements, ESPECIALLY DJANGO-REGISTRATION-REDUX

install version 1.2

command: pip install -U django-registration-redux==1.2

For TeamMembers: 
	When you pull the project and start working on it, make sure you have this pip list installed:
	(ehealth) E:\programirane\WAD\ehealth>pip freeze
	Django==1.7
	django-bootstrap-toolkit==2.15.0
	django-registration-redux==1.2
	Pillow==3.1.1
	IMPORTANT to have the same versions, otherwise django is mean and crashes.

So far implemented by Niki (git username: anakincho, student id: 2115451i):
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

So far implemented by Carly (2081252C):
	- updated base to contain categories sidebar and search bar like wireframes
	- had to edit some views to get this to show but everything appears to be working fine
	- removed search bar from login and registration pages
	- used JQuery for registration form validation
	- Updated about page to contain information about app and team
	- Put up a terms and conditions page
	- edit/delete categories
	- share ability
	- new design
	- pagination

So far implemented by Calum (2082101Y, calumyoung95):
	-Added bing_search.py
	-Added healthfinder_search.py
	-Added search view to views.py
	-Added search url to urls.py
	-Updated the base template to submit search form
	-Added medline_search.py
	-Used the readability files Niki set up to get appropriate values for each page
	-Created search.html which is redirected to if user searches
	-Population Script
	-toggle APIs with checkboxes
	-Added feature where user can only save pages if he/she is logged in
	-Moral Support
