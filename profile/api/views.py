from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializer import ProfileSerializer
from ..models import Profile
from rest_framework import views


class ProfileListCreateApi(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MyProfileListCreateAPIView(generics.ListAPIView):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({'detail': 'Authentication is required'}, status=status.HTTP_404_NOT_FOUND)
        profile = Profile.objects.filter(user_id=self.request.user.id).first()
        if profile:
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
