from django.db import models

# Create your models here.


class Header(models.Model):
    email_from = models.EmailField()
    email_title = models.TextField(max_length=250)

    def __str__(self):
        return self.email_from


class Content(models.Model):
    media = models.FileField(upload_to='media')


class Footer(models.Model):
    image = models.ImageField()
    link = models.URLField()

    def __str__(self):
        return self.link
