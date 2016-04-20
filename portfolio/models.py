from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Item(models.Model):
	date = models.DateField(max_length=200)
	name = models.CharField(max_length=200)
	detail = models.CharField(max_length=1000)
	detail2 = models.CharField(max_length=1000)