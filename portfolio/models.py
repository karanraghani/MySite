from django.db import models

class message(models.Model):
	name = models.CharField(max_length=50)
	email= models.EmailField(max_length=50)
	website = models.URLField(blank=True)
	text = models.TextField(max_length=300)

	def __str__(self):
		return (self.name,self.email)
