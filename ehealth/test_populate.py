import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehealth.settings')

import django
django.setup()

from ehealth_app.models import Category, Page, User

def add_user(username, email, password):
	user = User.objects.create_user(username=username, email=email, password=password)
	return user
	
def populate():
	add_user('john','john1@hotmail.co.uk', 'ada')
	
if __name__ == '__main__':
    print "Starting Test population script..."
    populate()
	