from django.db import models

# Create your models here.


class Header(models.Model):
    email_from = models.EmailField()
    email_title = models.CharField(max_length=250)

    def __str__(self):
        return self.email_title


class Content(models.Model):

    media = models.FileField()
    text = models.TextField(default='empty')

    def __str__(self):
        return self.text
    objects = models.Manager()
    media = models.FileField(upload_to='media')
    text = models.TextField()


class Footer(models.Model):
    objects = models.Manager()
    image = models.ImageField()
    link = models.URLField()

    def __str__(self):
        return self.link
