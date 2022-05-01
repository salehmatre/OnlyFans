from rest_framework import generics
from blogs.models import Comments
from .serializers import CommentsSerializer, UsersSerializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from CustomUsers.models import User


# Create your models here.

class CommentsView(generics.CreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticated]


# Users
class UsersView(generics.ListAPIView):
    serializer_class = UsersSerializers
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
