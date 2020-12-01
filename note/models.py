from django.db import models


class Note(models.Model):
    title = models.CharField("title", max_length=200)
    body = models.TextField("text")
    created = models.DateTimeField("created")
    updated = models.DateTimeField("updated")
    image = models.ImageField("image", upload_to="images")

    def __str__(self):
        return self.title
