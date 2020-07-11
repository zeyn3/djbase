from django.contrib import admin
from django.contrib.auth.models import User
from eventapp.models import Event, SkillGrid, Scope

# Register your models here.

admin.site.register(Event)
admin.site.register(SkillGrid)
admin.site.register(Scope)
