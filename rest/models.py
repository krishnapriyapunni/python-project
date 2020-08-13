from django.db import models


class Blogger(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=200)

   