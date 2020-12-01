from django.shortcuts import render
from django.views.generic import ListView

from .models import Note


class NoteListView(ListView):
    model = Note
    #def get_context_data(self, *, object_list=None, **kwargs):
    context_object_name = "notes"
    template_name = "note/main.html"
