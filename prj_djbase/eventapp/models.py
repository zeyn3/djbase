from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SkillGrid(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Scope(models.Model):
	name = models.CharField(max_length=200)
	skillgrid = models.ForeignKey(SkillGrid, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Event(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	title = models.CharField(max_length=200)
	scope = models.ForeignKey(Scope, on_delete=models.PROTECT)

	def __str__(self):
		return self.title
