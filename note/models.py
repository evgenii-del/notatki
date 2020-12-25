from django.db import models


class Note(models.Model):
    title = models.CharField("title", max_length=200)
    body = models.TextField("text")
    created = models.DateTimeField("created", blank=True, null=True)
    updated = models.DateTimeField("updated", blank=True, null=True)
    image = models.ImageField("image", upload_to="images", blank=True)

    def __str__(self):
        return self.title


class Folder(models.Model):
    title = models.CharField("title", max_length=200),
    icon = models.ImageField("icon", upload_to="images", blank=True),
    created = models.DateTimeField("created", blank=True, null=True),
    notes = models.ForeignKey(Note, blank=True, null=True)