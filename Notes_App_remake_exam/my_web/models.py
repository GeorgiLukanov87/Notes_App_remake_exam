from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=20, )
    last_name = models.CharField(max_length=20, )
    age = models.PositiveIntegerField()
    image_url = models.URLField()


class Note(models.Model):
    title = models.CharField(max_length=30, )
    image_url = models.URLField()
    content = models.TextField()
