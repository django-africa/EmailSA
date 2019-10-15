from django.contrib.auth.models import Group
from rest_framework import serializers 

from django.contrib.auth.models import User
from .models import UserProfile

# first we define the serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'user_profile'
        model = UserProfile
        fields = '__all__'
