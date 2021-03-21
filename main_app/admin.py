from django.contrib import admin
from main_app.models import Newsfeed

# Register your models here.


@admin.register(Newsfeed)
class NewsfeedAdmin(admin.ModelAdmin):
    pass
