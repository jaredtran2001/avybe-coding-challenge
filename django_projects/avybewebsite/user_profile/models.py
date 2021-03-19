from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=300, unique=True)
    inputFile = models.ImageField(null = True)