from django.urls import path

from . import views

urlpatterns = [
    path("", views.NoteListView.as_view(), name="notes-list"),
    path("create/", views.NoteCreateView.as_view(), name="notes-create"),
    path("<int:pk>/update/", views.NoteUpdateView.as_view(), name="notes-update"),
    path("<int:pk>/delete/", views.NoteDeleteView.as_view(), name="notes-delete")
]
