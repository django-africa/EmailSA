from rest_framework import serializers
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from newsletter.models import Header, Content, Footer
from EmailSa import settings
from newsletter.serializer import HeaderSerializer
from django.db import models
from django.urls import path
from newsletter.views import HeaderView

#Serializer.py
class HeaderSerializer(serializers.Serializer):
    email_from = serializers.EmailField()
    email_title = serializers.CharField(max_length=250)


class ContentSerializer(serializers.Serializer):
    media = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ('media',)

    def get_photo_url(self, content):
        request = self.context.get('request')
        media = content.media.url
        return request.build_absolute_url(media)


class FooterSerializer(serializers.Serializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Footer
        fields = ('image', 'link')

    def get_photo_url(self, footer):
        request = self.context.get('request')
        media = footer.image.url
        return request.build_absolute_url(media)

# Views.py
class HeaderView(APIView):
    def get(self, request):
        header = Header.objects.all()
        serializer = HeaderSerializer(header, many=True )
        return Response({'header': serializer.data})


class ContentView(APIView):
    def get(self, request):
        media = Content.objects.all()
        return Response({'media': media})


class FooterView(APIView):
    def get(self, request):
        footer = Footer.objects.all()
        return Response({'footer': footer})


# models.py
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


# urls.py
urlpatterns = [
    path('', HeaderView.as_view(), name='header'),
]
