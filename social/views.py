from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Create your views here.
from social.models import Posts, User, Likes, Comment
from social.serializers import PostsListSerializer, PostsCreateSerializer, UserListSerializer, LikesListSerializer, \
    LikesCreateSerializer, CommentListSerializer, CommentCreateSerializer


class PostsViews(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Posts.objects.filter(published=True).order_by('-updated_at')

    def get_serializer_class(self):
        if self.request and self.request.method == 'GET':
            return PostsListSerializer
        elif self.request and self.request.method == 'POST':
            return PostsCreateSerializer

    def create(self, request, *args, **kwargs):
        """
        Return posts ID after creating an article for the requesting user.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'posts_id': serializer.instance.id}, status=status.HTTP_201_CREATED)


class UserView(generics.ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request and self.request.method == 'GET':
            return UserListSerializer


class LikesViews(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Likes.objects.all()

    def get_serializer_class(self):
        if self.request and self.request.method == 'GET':
            return LikesListSerializer
        elif self.request and self.request.method == 'POST':
            return LikesCreateSerializer

    def create(self, request, *args, **kwargs):
        """
        Return article ID after creating an article for the requesting user.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'likes_id': serializer.instance.id}, status=status.HTTP_201_CREATED)


class CommentViews(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.request and self.request.method == 'GET':
            return CommentListSerializer
        elif self.request and self.request.method == 'POST':
            return CommentCreateSerializer

    def create(self, request, *args, **kwargs):
        """
        Return article ID after creating an article for the requesting user.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'comment_id': serializer.instance.id}, status=status.HTTP_201_CREATED)


class PostsDetailViews(generics.RetrieveDestroyAPIView):
    authentication_classes = ()
    permission_classes = ()

    def get_serializer_class(self):
        if self.request and self.request.method == 'GET':
            return PostsListSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('pk', None)
        return Posts.objects.filter(id=post_id)

