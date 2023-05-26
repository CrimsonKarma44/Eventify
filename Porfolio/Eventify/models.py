from django.db import models



class Events(models.Model):
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
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return str(self.name)

class Review(models.Model):
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    content = models.TextField()
    rate = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return str(self.name)

class Tickets(models.Model):
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    avail_status = models.BooleanField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return str(self.name)

class Payments(models.Model):
    ticket_id = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    price = models.FloatField()
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=60)


    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return str(self.name)
