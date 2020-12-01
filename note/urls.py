from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.NoteListView.as_view(), name="notes"),
    path("create/", views.CreateNoteView.as_view()),
    path("<int:pk>/delete/", views.NoteDeleteView.as_view(), name="delete-note")
]
