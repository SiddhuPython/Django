# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class instructor(models.Model):
	name = models.CharField(max_length=250)
	mobile = models.IntegerField()
	email = models.EmailField()
	info = models.TextField()

