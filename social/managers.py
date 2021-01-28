from django.db import models


# Managers to create the model objects in PosgresDB


class PostsManager(models.Manager):

    def create_posts(self, headline=None, content=None, published=False, category='UN', like=False,
                     author=None, **kwargs):
        """
        Post managers
        :param headline:
        :param content:
        :param published:
        :param category:
        :param like:
        :param author:
        :param kwargs:
        :return:
        """

        posts = self.model(headline=headline,
                           content=content,
                           published=published,
                           category=category,
                           author=author,
                           like=like)
        posts.save()
        return posts


class LikesManager(models.Manager):
    def create_likes(self, activity='NL', user=None, post=None, **kwargs):
        """
        Likes model to create teh like on the post
        :param activity:
        :param user:
        :param post:
        :param kwargs:
        :return:
        """
        likes = self.model(activity=activity, user=user, post=post)
        likes.save()
        return likes


class CommentsManager(models.Manager):
    def create_comments(self, comment_content=None, post=None, comment_published=True, **kwargs):
        """
        Comment object creation
        :param comment_content:
        :param comment_published:
        :param kwargs:
        :return:
        """
        comments = self.model(comment_content=comment_content,
                              post=post,
                              comment_published=comment_published)
        comments.save()
        return comments
