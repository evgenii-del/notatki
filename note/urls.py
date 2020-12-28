from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.NoteCreateView.as_view(), name="notes-create"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name="notes-detail"),
    path("<int:pk>/update/", views.NoteUpdateView.as_view(), name="notes-update"),
    path("<int:pk>/delete/", views.NoteDeleteView.as_view(), name="notes-delete"),
    path("<int:pk>/archive/", views.ArchiveNotes.as_view(), name="notes-archive"),
    path("archive/", views.NoteArchiveListView.as_view(), name="notes-archives"),
    path("", views.NotesSearchList.as_view(), name="notes-list"),
    path("<int:pk>/favorite/", views.FavoriteNotes.as_view(), name="notes-favorite"),
    path("favorites/", views.NoteFavoritesListView.as_view(), name="notes-favorites"),
]
