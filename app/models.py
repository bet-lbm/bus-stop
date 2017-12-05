from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Bus(models.Model):
	code = models.CharField(max_length=6)
	transport_company = models.CharField(max_length=200)
	
	def __str__(self):
		return self.transport_company	

class Stop(models.Model):
	name = models.CharField(max_length=200)
	reference = models.CharField(max_length=200)
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Route(models.Model):
	TIPO_CHOICES = (
        ('S', 'Subida'),
        ('B', 'Bajada'),   
    )
	route = models.ForeignKey(Bus)
	stop = models.ForeignKey(Stop)
	tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)

 	def __str__(self):
		return self.tipo
