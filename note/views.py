from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from django.urls import reverse
from .forms import NoteForm
from .models import Note


class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "note/main.html"


class CreateNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note/create.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("notes")


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    template_name = "note/delete.html"
