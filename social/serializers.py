from django.shortcuts import get_object_or_404
from rest_framework import serializers

from social.models import Posts, User, Likes, Comment


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'gender', 'birth_date', 'contact_address')
        read_only = ('id', 'contact_address')


class PostsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('headline', 'content', 'author_id', 'published', 'category',)

    def validate(self, attrs):
        headline = attrs.get('headline', None)
        content = attrs.get('content', None)
        published = attrs.get('published', True)
        category = attrs.get('category', None)

        if not headline and not content and not published and not category:
            error_msg = "desired fields may be missing from the request body"
            raise serializers.ValidationError(error_msg)
        return attrs

    def create(self, validated_data: dict) -> object:
        """
        Call the manager function to create an article.
        :param validated_data:
        :return:
        """
        request = self.context.get('request', None)
        headline = validated_data.get('headline', None)
        content = validated_data.get('content', None)
        author_id = request.data.get('author_id', None)
        author = get_object_or_404(User.objects.all(), id=author_id)
        published = validated_data.get('published', True)
        category = validated_data.get('category', None)

        return Posts.objects.create_posts(headline=headline,
                                          content=content,
                                          categories=category,
                                          published=published,
                                          author=author)


class LikesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ('id', 'activity', 'user', 'post',)
        read_only = ('id', 'user', 'post')


class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'headline', 'content', 'published', 'category', 'like', 'author')
        read_only = ('id', 'author')


class LikesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ('activity', 'user', 'post',)

    def validate(self, attrs):
        activity = attrs.get('activity', None)
        user = attrs.get('user', None)
        post = attrs.get('post', True)

        if activity and post and user:
            return attrs
        error_msg = "desired fields may be missing from the request body"
        raise serializers.ValidationError(error_msg)

    def create(self, validated_data: dict) -> object:
        """
        Creates likes objects
        :param validated_data:
        :return:
        """
        request = self.context.get('request', None)
        post = validated_data.get('post', None)
        activity = validated_data.get('activity', None)
        user = request.data.get('user', None)
        author = get_object_or_404(User.objects.all(), id=user)
        post = get_object_or_404(Posts.objects.all(), id=post.id)

        return Likes.objects.create_likes(activity=activity,
                                          user=author,
                                          post=post)


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'comment_published', 'post',)
        read_only = ('id', 'comment_content', 'post')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_content', 'comment_published', 'post',)

    def validate(self, attrs):
        comment_content = attrs.get('comment_content', None)
        comment_published = attrs.get('comment_published', None)
        post = attrs.get('post', None)

        if comment_content and comment_published and post:
            return attrs
        error_msg = "desired fields may be missing from the request body"
        raise serializers.ValidationError(error_msg)

    def create(self, validated_data: dict) -> object:
        """
        Create comments
        :param validated_data:
        :return:
        """
        comment_content = validated_data.get('comment_content', None)
        comment_published = validated_data.get('comment_published', False)
        post = validated_data.get('post', None)
        post = get_object_or_404(Posts.objects.all(), id=post.id)

        return Comment.objects.create_comments(comment_content=comment_content,
                                               comment_published=comment_published,
                                               post=post)
