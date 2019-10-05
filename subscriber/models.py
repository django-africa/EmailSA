from django.db import models
from users import models as Custom
# Create your models here.

class Subscriber(models.Model):
    objects = models.Manager()
    owner = models.OneToOneField(Custom.CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    interest = models.CharField(max_length=255)

class Profile(models.Model):
    objects = models.Manager()
    subscriber = models.OneToOneField(Subscriber, on_delete=models.CASCADE)
    total = models.IntegerField()
    title = models.CharField(max_length=255)
    time = models.TimeField()

