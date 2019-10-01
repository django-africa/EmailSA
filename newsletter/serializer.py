from rest_framework import serializers

# Header Serializer class
class HeaderSerializer(serializers.Serializer):
     email_from = serializers.EmailField()
     email_title = serializers.CharField(max_length=250)


# Content Serializer class
class ContentSerializer(serializers.Serializer):
    media = serializers.FileField()


# Footer Serializer class
class FooterSerializer(serializers.Serializer):
    image = serializers.ImageField()
    link = serializers.URLField()