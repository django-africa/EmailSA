from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    interest = models.CharField(max_length=255)

class SubscriberProfile(models.Model):
    subscriber = models.OneToOneField(Subscriber, on_delete=models.CASCADE)
    total = models.IntegerField()
    title = models.CharField(max_length=255)
    time = models.TimeField()

