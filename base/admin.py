# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task) #registering the model into admin pannel
