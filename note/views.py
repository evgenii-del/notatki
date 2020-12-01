from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from .models import Note

from .models import Note


class NoteListView(ListView):
    model = Note
    # def get_context_data(self, *, object_list=None, **kwargs):
    context_object_name = "notes"
    template_name = "note/main.html"


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    template_name = "note/delete.html"
