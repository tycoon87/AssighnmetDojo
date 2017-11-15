# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

class Ninja(models.Model):
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Dojo = models.ForeignKey(Dojo, related_name = "Ninjas")
