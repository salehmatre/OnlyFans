from django.urls import path
from .views import (HomePage, DetailPage, TagView,
                    RegisterView, LogInView, LogOutView)

urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path("similar/tags/<str:tag>/", TagView.as_view(), name='tagview'),
    path("read/<int:pk>/", DetailPage.as_view(), name='read'),
    path('signup/user/', RegisterView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout')
]
