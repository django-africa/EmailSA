"""EmailSa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from users import viewsets, views
from newsletter import viewsets as newsview
from subscriber import viewsets as subview

from .views import CustomAuthToken
from rest_framework.authtoken import views as oviews


router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet, basename='user')
router.register(r'profile', viewsets.ProfileViewSet, basename='Profile')

router.register(r'header', newsview.HeaderViewSet)
router.register(r'content', newsview.ContentViewSet)
router.register(r'footer', newsview.FooterViewSet)

router.register(r'subscriber', subview.SubscribeViewSet)
router.register(r'subscriberProfile', subview.ProfileViewSet)


urlpatterns = [
    url(r'', include(router.urls), name=''),
    url(r'signup/', views.signup, name='signup'),
    url(r'api-auth/', include('rest_framework.urls')),
    url(r'api-token-auth/',  oviews.obtain_auth_token),
    url(r'admin/', admin.site.urls),
]