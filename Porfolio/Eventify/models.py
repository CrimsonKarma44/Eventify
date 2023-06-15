from django.db import models
from django.contrib.auth.models import User

types_genre = [
    ('Con', 'Concert'),
    ('Com', 'Communities'),
    ('Cl', 'Classes'),
    ('P', 'Parties'),
    ('S', 'Sport'),
]


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    type = models.CharField(
        max_length=60, choices=types_genre, default='Event')
    location = models.CharField(max_length=200)
    img = models.ImageField(upload_to='banner', default=None)

    start = models.DateTimeField()
    end = models.DateTimeField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start', '-end']

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    # name = models.CharField(max_length=200)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=60, choices=types_genre, default='Event')
    # type = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=100)
    public_key = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # Add any additional fields as needed

    def __str__(self):
        return self.user.username
