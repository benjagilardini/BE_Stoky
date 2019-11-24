# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stock (models.Model):
    nombre = models.CharField(max_length = 15, null = False)
    descripcion  = models.CharField(max_length = 30, null = False)
    cantidad = models.IntegerField(null=False)

    def __str__ (self):
        return '{}, {}'.format(self.nombre, self.cantidad)
