from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Log(models.Model):
	time = models.CharField(max_length=14)
	temp = models.IntegerField()
	humi = models.IntegerField()
	
	def __str__(self):
		return (self.time[:4]+'/'+self.time[4:6]+'/'+
			self.time[6:8]+' '+self.time[8:10]+':'+
			self.time[10:12]+':'+self.time[12:])
