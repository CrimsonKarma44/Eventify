from django.db import models

types_genre = [
    ('P', 'Party'),
    ('E', 'Event'),
    ('S', 'Show'),
    ('B', 'Bonfire'),
]


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=60, choices=types_genre, default='Event')
    location = models.CharField(max_length=200)

    start = models.DateTimeField(auto_now=True)
    end = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)


class Category(models.Model):
    # name = models.CharField(max_length=200)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.CharField(max_length=60, choices=types_genre, default='Event')
    # type = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.event_id)

