from django.test import RequestFactory, TestCase
from django.urls import reverse

from .models import Note


class HomePageTest(TestCase):
    def test_note_list_class(self):
        response = self.client.get(reverse('notes-list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['notes'], [])

    def test_note_create_class(self):
        self.client.post('/notes/create/', {'title': "Test title", 'body': "Test body"})
        self.assertEqual(Note.objects.last().title, "Test title")

    def test_note_delete_class(self):
        note = Note.objects.create(title="Test delete title", body="Test delete body")
        response = self.client.get(reverse('notes-delete', kwargs={'pk': note.pk}))
        self.assertContains(response, "Test delete title")

    def test_note_update_class(self):
        note = Note.objects.create(title="Test update title", body="Test update body")
        self.client.post(reverse('notes-update', kwargs={'pk': note.pk}),
                         {'title': "Test update title 2", 'body': "Test update body 2"})
        self.assertEqual(Note.objects.last().title, "Test update title 2")
