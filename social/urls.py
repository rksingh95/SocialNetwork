from django.urls import path

from .views import PostsViews, UserView, LikesViews, PostsDetailViews, CommentViews

urlpatterns = [
    path("posts/", PostsViews.as_view(), name='post'),
    path("likes/", LikesViews.as_view(), name='likes'),
    path("comments/", CommentViews.as_view(), name='comments'),
    path("posts/detail/<uuid:pk>/", PostsDetailViews.as_view(), name='posts-detail'),
    path("users/", UserView.as_view(), name='user'),

]