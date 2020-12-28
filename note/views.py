from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from search_views.filters import BaseFilter
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse
from .forms import NoteForm
from .models import Note


class NoteConfigView(View):
    model = Note

    def get_success_url(self):
        return reverse("notes-list")


class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "note/main.html"


class NoteArchiveListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "note/archive.html"


class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "note/detail.html"


class NoteCreateView(NoteConfigView, CreateView):
    form_class = NoteForm
    template_name = "note/create.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("notes-list")

class NoteUpdateView(NoteConfigView, UpdateView):
    form_class = NoteForm
    template_name = "note/update.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("notes-list")

class NoteDeleteView(NoteConfigView, DeleteView):
    template_name = "note/delete.html"

    def get_success_url(self):
        return reverse("notes-list")


class NotesFilter(BaseFilter):
    search_fields = {
        'search_text': ['body', 'title'],
        #'search_title': ['title'],
    }


class NotesSearchList(SearchListView):
    model = Note
    template_name = "note/notes_list.html"
    form_class = NoteSearchForm
    filter_class = NotesFilter


class ArchiveNotes(View):
    def get(self, request, pk):
        note = Note.objects.get(pk=pk)
        is_archive = note.archive
        note.archive = not is_archive
        note.save()
        return redirect(note.get_absolute_url())
