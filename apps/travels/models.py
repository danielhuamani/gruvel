from django.db import models

# Create your models here.
class Travel(models.Model):
	title = models.CharField(max_length=140)
	origin = models.CharField(max_length=140)
	destination = models.CharField(max_length=140)
	depart_date = models.DateField()
	return_date = models.DateField(blank=True)

	def __str__(self):
		return self.title
