from rest_framework import serializers 

from .models import Subscriber, Profile

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'subscriber_profile'
        model = Profile
        fields = '__all__'

