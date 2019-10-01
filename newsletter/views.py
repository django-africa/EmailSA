from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Header, Content, Footer
from .serializer import HeaderSerializer, FooterSerializer, ContentSerializer



# Create your views here.


class HeaderView(APIView):
    def get(self, request):
        header = Header.objects.all()
        serializer = HeaderSerializer(header, many=True )
        return Response({'header': serializer.data})


class ContentView(APIView):
    def get(self, request):
        media = Content.objects.all()
        serializer = ContentSerializer(media, many=True)
        return Response({'media': serializer.data})


class FooterView(APIView):
    def get(self, request):
        footer = Footer.objects.all()
        serializer = FooterSerializer(footer, many=True)
        return Response({'footer': serializer.data})
