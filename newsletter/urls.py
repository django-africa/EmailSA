from django.urls import path
from .views import HeaderView, ContentView, FooterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HeaderView.as_view(), name='header'),
    path('content/', ContentView.as_view(), name='content'),
    path('footer/', FooterView.as_view(), name='footer')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
