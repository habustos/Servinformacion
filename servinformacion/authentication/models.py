# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.

class SessionKey(models.Model):
    user = models.OneToOneField(User,primary_key=True)
    key = models.CharField(max_length=255)
