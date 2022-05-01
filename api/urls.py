from django.urls import path
from .views import CommentsView, UsersView

urlpatterns = [
    path('v1/comments/create/', CommentsView.as_view()),
    path('v1/users/', UsersView.as_view()),
]