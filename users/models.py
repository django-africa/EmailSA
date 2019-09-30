from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save


def get_domain(sender, instance, **kwargs):
    if not instance.domain_name:
        instance.domain_name = instance.email.split('@')[1]

def validate_phone(value):
    if len(str(value)) > 13:
        raise ValidationError(_('Phone number cannot be longer than 13'))

class CustomUser(AbstractUser):
    domain_name = models.CharField(max_length=255, editable=False)

pre_save.connect(get_domain, sender=CustomUser)
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField()
    phone = models.IntegerField(validators=[validate_phone])
    address = models.CharField(max_length=255)
    country = CountryField()

