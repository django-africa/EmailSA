from rest_framework import viewsets
from .models import Subscriber, Profile
from .serializers import SubscriberSerializer, ProfileSerializer


class SubscribeViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer