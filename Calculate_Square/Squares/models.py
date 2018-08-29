# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class square(models.Model):
    number = models.IntegerField()
    sqr = models.IntegerField()
