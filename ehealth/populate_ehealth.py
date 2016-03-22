__author__ = 'Nikolay & Calum'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehealth.settings')

import django
django.setup()

from ehealth_app.models import Category, Page

#Populating function
#All the data created from here is for testing purposes!
def populate():

	add_user('bob','bobkennedy@hotmail.co.uk', 'bob')
	
	add_user('jill','jillvalentine@hotmail.co.uk', 'jill')

	diabetes_cat = add_cat('Diabetes', 'jill') #creates a category with name Diabetes, by the user testUser
    # Adds a page to our Diabetes category with all the fields
	add_page(cat                = diabetes_cat,
			title              = 'Preventing Diabetes: Questions for the doctor',
			url                = 'http://healthfinder.gov/HealthTopics/Category/doctor-visits/talking-with-the-doctor/preventing-diabetes-questions-for-the-doctor',
			flesch_score       = 12.5,
			polarity_score     = 10.2,
			subjectivity_score = 13.6,
			shared = True)
			 
	add_page(cat                = diabetes_cat,
			title              = 'What are the Types of Diabetes and Prediabetes?',
			url                = 'http://diabetes.about.com/od/whatisdiabetes/p/whatisdiabetes.html',
			flesch_score       = 60.31,
			polarity_score     = -0.5,
			subjectivity_score = 0.3,
			shared = False)
			 
	add_page(cat                = diabetes_cat,
			title              = 'Diabetes Insipidus',
			url                = 'https://www.nlm.nih.gov/medlineplus/diabetesinsipidus.html',
			flesch_score       = 71.31,
			polarity_score     = -0.5,
			subjectivity_score = 0.3,
			shared = True)

	flu_cat = add_cat('Flu', 'jill') #creates a category with name Flu, by the user testUser
    #adds a page to our Flu category with all the fields
	add_page(cat                = flu_cat,
			title              = 'Prepare for a Flu Pandemic',
			url                = 
'http://healthfinder.gov/HealthTopics/Category/everyday-healthy-living/safety/prepare-for-a-flu-pandemic',
			flesch_score       = 8.3,
			polarity_score     = 7.4,
			subjectivity_score = 10.8,
			shared = True)
			 
	add_page(cat                = flu_cat,
			title              = 'Flu in Adults: How Long Does the Flu Last? - eMedicineHealth',
			url                = 'http://www.emedicinehealth.com/flu_in_adults/article_em.html',
			flesch_score       = 95.17,
			polarity_score     = -0.6,
			subjectivity_score = 1.0,
			shared = True)

	cancer_cat = add_cat('Cancer', 'bob')
	add_page(cat                = cancer_cat,
			title              = 'Mammography',
			url                = 'https://www.nlm.nih.gov/medlineplus/mammography.html',
			flesch_score       = 77.23,
			polarity_score     =  -0.0557142857143,
			subjectivity_score = 0.417619047619,
			shared = False)
	
	add_page(cat                = cancer_cat,
			title              = 'Breast Cancer Kent',
			url                = 'http://www.breastcancerkent.org.uk/',
			flesch_score       = 80.28,
			polarity_score     = -0.25,
			subjectivity_score = 0.25,
			shared = False)
	
	hiv_cat = add_cat('HIV', 'bob')
	add_page(cat                = hiv_cat,
		title              = 'HIV - Simple English Wikipedia, the free encycolpedia',
		url                = 'https://simple.wikipedia.org/wiki/HIV',
		flesch_score       = 43.06,
		polarity_score     = 0.0,
		subjectivity_score = -0.1,
		shared = True)
	
	
	add_page(cat                = hiv_cat,
			title              = "Kaposi's Sarcoma",
			url                = 'https://www.nlm.nih.gov/medlineplus/kaposissarcoma.html',
			flesch_score       = 68.77,
			polarity_score     =  -0.173958333333,
			subjectivity_score =  0.392708333333,
			shared = True)
	

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, flesch_score, polarity_score, subjectivity_score, shared):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url=url
	p.flesch_score = flesch_score
	p.polarity_score = polarity_score
	p.subjectivity_score = subjectivity_score
	p.shared = shared
	p.save()
	return p

def add_cat(name, user, shared):
	c = Category.objects.get_or_create(name=name, user=user)[0]
	c.shared = shared
	return c

def add_user(username, email, password):
	user = User.objects.create_user(username=username, email=email, password=password)
	return user
	
	
if __name__ == '__main__':
    print "Starting eHealth population script..."
    populate()