from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



def validate_phone(value):
    if len(str(value)) > 13:
        raise ValidationError(_('Phone number cannot be longer than 13'))
    

# Just before saving the CustomUser Moodel gets the domain name 
# from the  AbstractUsers' email Address using the pre save model signal


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserProfile(models.Model):
        objects = models.Manager()
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        avatar = models.ImageField()
        phone = models.IntegerField(validators=[validate_phone])
        address = models.CharField(max_length=255)
        country = CountryField()