from django.contrib import admin
from .models import Event, Comment, Speaker

# Register your models here.

admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Speaker)
