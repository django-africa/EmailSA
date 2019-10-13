from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Header, Content, Footer
from .serializer import HeaderSerializer, ContentSerializer, FooterSerializer


class HeaderViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

class ContentViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class FooterViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer