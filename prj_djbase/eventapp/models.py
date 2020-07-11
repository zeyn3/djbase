from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Type(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Event(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	title = models.CharField(max_length=200)
	type = models.ForeignKey(Type, on_delete=models.PROTECT)

	def __str__(self):
		return self.title
