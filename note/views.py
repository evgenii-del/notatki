from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from search_views.filters import BaseFilter
from django.urls import reverse
from search_views.views import SearchListView
from taggit.models import Tag
from .models import Note, Folder
from .forms import NoteForm, NoteSearchForm, FolderForm, FolderSearchForm


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class NoteConfigView(View):
    model = Note

    def get_success_url(self):
        return reverse("notes-list")


class NoteListView(TagMixin, ListView):
    model = Note
    context_object_name = "notes"
    template_name = "note/main.html"
    queryset = Note.objects.all()


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


class NoteUpdateView(NoteConfigView, UpdateView):
    form_class = NoteForm
    template_name = "note/update.html"

    def form_valid(self, form):
        return super().form_valid(form)


class NoteDeleteView(NoteConfigView, DeleteView):
    template_name = "note/delete.html"

    def get_success_url(self):
        return reverse("notes-list")


class ArchiveNotes(View):
    def get(self, request, pk):
        note = Note.objects.get(pk=pk)
        is_archive = note.archive
        note.archive = not is_archive
        note.save()
        return redirect(note.get_absolute_url())


class FavoriteNotes(View):
    def get(self, request, pk):
        note = Note.objects.get(pk=pk)
        is_favorite = note.favorite
        note.favorite = not is_favorite
        note.save()
        return redirect(note.get_absolute_url())


class NoteFavoritesListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "note/favorites.html"


class NotesFilter(BaseFilter):
    search_fields = {
        'search_text': ['body', 'title'],
    }


class NotesSearchList(SearchListView):
    model = Note
    template_name = "note/notes_list.html"
    form_class = NoteSearchForm
    filter_class = NotesFilter


class PostFilterView(NoteListView):
    model = Note
    template_name = "note/notes_list.html"

    def get_queryset(self):
        print(self.kwargs["pk"])
        if self.kwargs["pk"] == 1:
            return Note.objects.all().order_by("-created")
        elif self.kwargs["pk"] == 2:
            return Note.objects.all().order_by("created")


class NoteSortByDate(ListView):
    model = Note
    template_name = "note/notes_list.html"


class FolderConfigView(View):
    model = Folder

    def get_success_url(self):
        return reverse("folders-list")


class FolderCreateView(FolderConfigView, CreateView):
    form_class = FolderForm
    template_name = "folder/create.html"

    def form_valid(self, form):
        return super().form_valid(form)


class FolderFilter(BaseFilter):
    search_fields = {
        'search_text': ['title']
    }


class FolderSearchList(SearchListView):
    model = Folder
    template_name = "folder/folders_list.html"
    form_class = FolderSearchForm
    filter_class = FolderFilter


class AddNoteToFolder:()

class TagIndexView(TagMixin, ListView):
    template_name = 'note/notes_list.html'
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(tags__slug=self.kwargs.get("slug"))
