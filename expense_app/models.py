# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Expense(models.Model):
    title = models.CharField(max_length=100)
    cost = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title + " " + str(self.date)
