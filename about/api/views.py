from rest_framework import generics
from .serializer import AboutSerializer
from ..models import About


class AboutListCreativeAPIView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

#
# class AboutRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = About.objects.all()
#     serializer_class = AboutSerializer
