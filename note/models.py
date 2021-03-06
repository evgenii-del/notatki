from django.urls import reverse
from taggit.managers import TaggableManager
from django.db import models


class Note(models.Model):
    title = models.CharField("title", max_length=200)
    body = models.TextField("text")
    created = models.DateTimeField("created", auto_now=True)
    updated = models.DateTimeField("updated", auto_now_add=True)
    image = models.ImageField("image", upload_to="images", blank=True)
    archive = models.BooleanField("archive", default=False)
    favorite = models.BooleanField("favorite", default=False)
    tags = TaggableManager(blank=True, verbose_name="tags")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes-detail', kwargs={'pk': self.pk})


class Folder(models.Model):
    note = models.ManyToManyField(Note, related_name='notatka')
    title = models.CharField("title", max_length=200)
    created = models.DateTimeField("created", auto_now_add=True)
    icon = models.ImageField("image", upload_to="images", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
