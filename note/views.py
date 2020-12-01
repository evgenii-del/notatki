from django.views.generic import ListView, DeleteView, CreateView, UpdateView, View
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
