from django.urls import path
from rest_framework.authtoken import views
from .views import MyProfileListCreateAPIView


urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('my/profile/', MyProfileListCreateAPIView.as_view())
]
