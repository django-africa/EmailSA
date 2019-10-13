from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import To
ken
from django.template.defaultfilters import slugify


def get_domain(sender, instance, **kwargs):
    #This gets domain name from AbstractUsers' email field
    if not instance.domain_name:
        instance.domain_name = instance.email.split('@')[1]


def validate_phone(value):
    if len(str(value)) > 13:
        raise ValidationError(_('Phone number cannot be longer than 13'))


class CustomUser(AbstractUser):
    domain_name = models.CharField(max_length=255, editable=False)
    slug = models.SlugField(max_length=300, verbose_name = "user_slug", null=True, blank =True)# --------------->   

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        return super(CustomUser, self).save(*args, **kwargs)
    
# Just before saving the CustomUser Moodel gets the domain name 
# from the  AbstractUsers' email Address using the pre save model signal
pre_save.connect(get_domain, sender=CustomUser)



@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Profile(models.Model):
        objects = models.Manager()
        user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
        avatar = models.ImageField()
        phone = models.IntegerField(validators=[validate_phone])
        address = models.CharField(max_length=255)
        country = CountryField()
