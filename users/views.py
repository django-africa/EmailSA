# from django.contrib.auth.models import Group

# from .models import CustomUser
# from .serializers import UserSerializer, GroupSerializer

# from rest_framework import generics, permissions


# # Create the API views
# class UserList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer


# class UserDetails(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer


# class GroupList(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasScope]
#     required_scopes = ['groups']
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer