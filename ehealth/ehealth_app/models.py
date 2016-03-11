from django.db import models

#our database model for the Categories
class Category(models.Model):
    #fields for the table
    user = models.CharField(max_length=128, unique = False) # 1 user can create multiple categories!
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

#our database model for the Saved Pages
class Page(models.Model):

    #fields for the table
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    flesch_score = models.FloatField(default=0)
    polarity_score = models.FloatField(default = 0)
    subjectivity_score = models.FloatField(default = 0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title