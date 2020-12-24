from django.urls import reverse

from django.db import models


class Note(models.Model):
    title = models.CharField("title", max_length=200)
    body = models.TextField("text")
    created = models.DateTimeField("created", auto_now_add=True)
    updated = models.DateTimeField("updated", auto_now=True)
    image = models.ImageField("image", upload_to="images", blank=True)
    archive = models.BooleanField("archive", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes-detail', kwargs={'pk': self.pk})
