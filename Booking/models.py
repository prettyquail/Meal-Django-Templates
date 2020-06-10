from django.db import models

# Create your models here.
class Breakfast(models.Model):
	dishname=models.CharField(max_length=60)
	img=models.ImageField()
	desc=models.CharField(max_length=200)
	price=models.IntegerField()

class Lunch(models.Model):
	dishname=models.CharField(max_length=60)
	img=models.ImageField()
	desc=models.CharField(max_length=200)
	price=models.IntegerField()

class Dinner(models.Model):
	dishname=models.CharField(max_length=60)
	img=models.ImageField()
	desc=models.CharField(max_length=200)
	price=models.IntegerField()

class Register(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField(max_length=200)
	phoneno=models.IntegerField(max_length=10)
	persons=models.IntegerField()
	time=models.TimeField()
	date=models.DateField()


class Contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField(max_length=200)
	phoneno=models.IntegerField(max_length=10)
	message=models.TextField()