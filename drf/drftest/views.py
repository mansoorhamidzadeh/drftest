from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import drfTest
from .serializers import drfTestSerilizer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly


@api_view(["GET"])  # new
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "drflist": reverse("drf-list", request=request, format=format),
        }
    )


class defListView(generics.ListCreateAPIView):
    queryset = drfTest.objects.all()
    serializer_class = drfTestSerilizer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class drfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = drfTest.objects.all()
    serializer_class = drfTestSerilizer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
