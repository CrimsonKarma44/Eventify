from django.db import models

# Create your models here.
class Events(models.Model):
    id = models.CharField(max_length=60)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    start = models.DateTimeField(auto_now=True)
    end = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return str(self.name)

class Categories(models.Model):
    id = models.CharField(max_length=60)
    # event_id = models.ForeignKey(Events)
    type = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return str(self.name)

class Review(models.Model):
    id = models.CharField(max_length=60)
    # event_id = models.CharField(max_length=60)
    email = models.CharField(max_length=200)
    content = models.TextField()
    rate = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return str(self.name)

class Tickets(models.Model):
    id = models.CharField(max_length=60)
    # event_id = models.CharField(max_length=60)
    name = models.CharField(max_length=200)
    price = models.FloatField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return str(self.name)

class Payments(models.Model):
    id = models.CharField(max_length=60)
    ticket_id = models.CharField(max_length=60)
    price = models.FloatField()
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=60)


    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return str(self.name)
