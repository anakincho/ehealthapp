from django.db import models
from django.template.defaultfilters import slugify

#our database model for the Categories
class Category(models.Model):
    #fields for the table
    user = models.CharField(max_length=128, unique = False) # 1 user can create multiple categories!
    name = models.CharField(max_length=128, unique=True)
    shared = models.BooleanField(default = False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
                # Uncomment if you don't want the slug to change every time the name changes
                #if self.id is None:
                        #self.slug = slugify(self.name)
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)


    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

#our database model for the Saved Pages
class Page(models.Model):

    #fields for the table
    user = models.CharField(max_length=128, unique= False) #We need this in order to show the non shared pages(from the current user)                                                                                                           # to the current user
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    flesch_score = models.FloatField(default=0)
    polarity_score = models.FloatField(default = 0)
    subjectivity_score = models.FloatField(default = 0)
    shared = models.BooleanField(default = False)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title