from django.db import models

# Create your models here.

class Categories(models.Model):
    id = models.CharField(max_length=60)

class Review(models.Model)):
    id = models.CharField(max_length=60)
    pass

class Events(models.Model):
    id = models.CharField(max_length=60)
    pass

class Payments(models.Model):
    id = models.CharField(max_length=60)
    pass

class Tickets(models.Model):
    id = models.CharField(max_length=60)
    pass