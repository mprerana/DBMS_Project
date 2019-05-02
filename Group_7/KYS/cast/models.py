from django.db import models

# Create your models here.
class profession(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class cast(models.Model):
	GENDER = (
			('Male','Male'),
			('Female','Female'),
			('Others','Others'),
		)
	name = models.CharField(max_length=120)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=15, choices=GENDER)
	dob = models.DateField()
	profession = models.ManyToManyField(profession)
	birthPlace = models.CharField(max_length=1000)
	biography = models.CharField(max_length=1000)
	photo = models.ImageField(upload_to='actors',blank=True)
	maritalStatus = models.CharField(max_length=120)
	origin = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class directors(models.Model):
	name = models.CharField(max_length=120)
	def __str__(self):
		return self.name

class director(models.Model):
	GENDER = (
			('Male','Male'),
			('Female','Female'),
			('Others','Others'),
		)
	name = models.CharField(max_length=120)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=15, choices=GENDER)
	dob = models.DateField()
	profession = models.ManyToManyField(profession)
	birthPlace = models.CharField(max_length=1000)
	biography = models.CharField(max_length=1000)
	photo = models.ImageField(upload_to='actors',blank=True)
	maritalStatus = models.CharField(max_length=120)
	origin = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class actors(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name

class producer(models.Model):
	GENDER = (
			('Male','Male'),
			('Female','Female'),
			('Others','Others'),
		)
	name = models.CharField(max_length=120)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=15, choices=GENDER)
	dob = models.DateField()
	profession = models.ManyToManyField(profession)
	birthPlace = models.CharField(max_length=1000)
	biography = models.CharField(max_length=1000)
	photo = models.ImageField(upload_to='actors',blank=True)
	maritalStatus = models.CharField(max_length=120)
	origin = models.CharField(max_length=100)

	def __str__(self):
		return self.name
