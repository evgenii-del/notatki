from django.contrib import admin

from .models import Note, Folder

admin.site.register(Note)
admin.site.register(Folder)
