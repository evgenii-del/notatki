from abc import ABC
from search_views.filters import BaseFilter

from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse
from search_views.views import SearchListView

from .forms import NoteForm, NoteSearchForm
from .models import Note


class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "note/main.html"


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note/create.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("notes-list")


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "note/update.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("notes-list")


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "note/delete.html"

    def get_success_url(self):
        return reverse("notes-list")


class NotesFilter(BaseFilter, ABC):
    search_fields = {
        'search_text': ['body'],
        'search_title': ['title'],

    }


class NotesSearchList(SearchListView):
    model = Note
    # paginate_by = 30
    template_name = "note/notes_list.html"
    form_class = NoteSearchForm
    filter_class = NotesFilter
