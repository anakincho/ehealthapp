from django.contrib import admin
from ehealth_app.models import Category, Page

# Used to customize the admin panel
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'shared', 'user')

# Used to customize the admin panel
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'shared','url', 'flesch_score', 'polarity_score', 'subjectivity_score')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)



