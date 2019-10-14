from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _






def validate_phone(value):
    if len(str(value)) > 13:
        raise ValidationError(_('Phone number cannot be longer than 13'))
    

# Just before saving the CustomUser Moodel gets the domain name 
# from the  AbstractUsers' email Address using the pre save model signal





class UserProfile(models.Model):
        objects = models.Manager()
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        avatar = models.ImageField()
        phone = models.IntegerField(validators=[validate_phone])
        address = models.CharField(max_length=255)
        country = CountryField()


# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)


