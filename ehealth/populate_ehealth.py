__author__ = 'Nikolay'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehealth.settings')

import django
django.setup()

from ehealth_app.models import Category, Page

#Populating function
#All the data created from here is for testing purposes!
def populate():

    diabetes_cat = add_cat('Diabetes', 'testUser') #creates a category with name Diabetes, by the user testUser
    # Adds a page to our Diabetes category with all the fields
    add_page(cat                = diabetes_cat,
             title              = 'Preventing Diabetes: Questions for the doctor',
             url                = 'http://healthfinder.gov/HealthTopics/Category/doctor-visits/talking-with-the-doctor/preventing-diabetes-questions-for-the-doctor',
             flesch_score       = 12.5,
             polarity_score     = 10.2,
             subjectivity_score = 13.6
    )

    flu_cat = add_cat('Flu', 'testUser') #creates a category with name Flu, by the user testUser
    #adds a page to our Flu category with all the fields
    add_page(cat                = flu_cat,
             title              = 'Prepare for a Flu Pandemic',
             url                = 'http://healthfinder.gov/HealthTopics/Category/everyday-healthy-living/safety/prepare-for-a-flu-pandemic',
             flesch_score       = 8.3,
             polarity_score     = 7.4,
             subjectivity_score = 10.8
    )

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, flesch_score, polarity_score, subjectivity_score):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.flesch_score = flesch_score
    p.polarity_score = polarity_score
    p.subjectivity_score = subjectivity_score
    p.save()
    return p

def add_cat(name, user):
    c = Category.objects.get_or_create(name=name, user=user)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()