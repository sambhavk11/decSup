from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.TextField(max_length=30)
    category = models.TextField(max_length=50)


class Category(models.Model):
    topic = models.TextField(max_length=50)
    area = models.TextField(max_length=50)
    subject = models.TextField(max_length=50)
    weight = models.PositiveIntegerField()
