from django.contrib import admin
from django.contrib.auth.models import User
from eventapp.models import Event, Type, Category

# Register your models here.

admin.site.register(Event)
admin.site.register(Type)
admin.site.register(Category)
