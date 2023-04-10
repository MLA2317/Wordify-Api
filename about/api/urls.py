from django.urls import path
from .views import AboutListCreativeAPIView


urlpatterns = [
    path('list-create/', AboutListCreativeAPIView.as_view()),
]