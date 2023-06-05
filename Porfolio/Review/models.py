from django.db import models
from Eventify.models import Event

# Create your models here.
class Review(models.Model):
    # name = models.CharField(max_length=200)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    content = models.TextField()
    rate = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.event_id)
