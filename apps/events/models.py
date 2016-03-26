from django.db import models

# Create your models here.
class Event(models.Model):
	photo = models.ImageField(upload_to='events/photos', blank=True)
	name = models.CharField(max_length=140)
	location = models.CharField(max_length=140)
	date_time = models.DateTimeField()
	description = models.TextField()

	def __str__(self):
		return self.name