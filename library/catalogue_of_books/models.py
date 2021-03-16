from django.db import models
from django.conf import settings
from django.utils import timezone

class Book(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateTimeField()
	price = models.IntegerField()
	authors = models.CharField(max_length=200)
	comments = models.CharField(max_length=200, default='SOME STRING')

	def publish(self):
        	self.published_date = timezone.now()
        	self.save()

	class Meta1:
		verbose_name = 'Книги'


