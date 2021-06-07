from django.shortcuts import render
from rest_framework import generics, permissions
from apiapp import serializers
from apiapp.models import Post


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostCreateView(generics.CreateAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class LikeDislikeView(generics.UpdateAPIView):
#     queryset = LikeDislike.objects.all()
#     permission_classes = (permissions.IsAuthenticated, )
#
