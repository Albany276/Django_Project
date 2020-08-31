from django.contrib import admin
from .models import NewsStory #making NewsStory avail to admin

# Register your models here.
admin.site.register(NewsStory) #registering the table NewsStory so it is visible on te admin page

