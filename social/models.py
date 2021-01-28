import uuid

from django.db import models

# Create your models here.
from social.managers import LikesManager, PostsManager, CommentsManager


class Address(models.Model):
    """
    Address model class. Only supported via admin creation
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    street = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(models.Model):
    """
    User model to create user object
    Note user creation only supported via admin and so is its address object
    """
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    UNKNOWN = "U"

    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
        (UNKNOWN, "Unknown"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(max_length=255, verbose_name='email address', unique=True, help_text='User Email')
    first_name = models.CharField(max_length=255, blank=True, editable=True, help_text=' User First Name')
    last_name = models.CharField(max_length=255, blank=True, help_text='User Last Name')
    gender = models.CharField(max_length=16, choices=GENDER_CHOICES, default=UNKNOWN,
                              help_text='Gender choice M, F, O, U')
    birth_date = models.DateField(null=True, help_text=' Date of birth of user')
    contact_address = models.OneToOneField(Address, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                           help_text='User Contact address related to address class ')


class Posts(models.Model):
    """
    Posts model object that hold the detailed post and can also be authored by user and divided in categories
    """
    SOCIAL = "S"
    PERSONAL = "P"
    INTERNATIONAL = "I"
    SPORTS = "SP"
    FUN = "F"
    UNIDENTIFIED = 'UI'
    CATEGORY_CHOICES = [
        (SOCIAL, "Social"),
        (PERSONAL, "Personal"),
        (INTERNATIONAL, "International"),
        (SPORTS, "Sports"),
        (FUN, "Fun"),
        (UNIDENTIFIED, "Unidentified"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    headline = models.CharField(max_length=255, unique=True, blank=False, null=False, help_text='Post headline')
    content = models.TextField(blank=False, null=False, help_text='Post content')
    published = models.BooleanField(default=True)
    category = models.CharField(max_length=16, choices=CATEGORY_CHOICES, default=UNIDENTIFIED,
                                help_text='Category choice S, P, I, F, SP, UI')
    like = models.BooleanField(default=False)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_post',
                               related_query_name='user_posts',
                               blank=False,
                               null=False,
                               help_text='Posts authored by user')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostsManager()

    def __str__(self):
        return "id: %s author: %s" % (self.id, self.author.email)


class Likes(models.Model):
    """
    Likes model keeps track of post being liked or not
    """
    LIKE_UP = 'LU'
    LIKE_DOWN = 'LD'
    NO_LIKE = 'NL'
    LIKE_CHOICES = (
        (LIKE_UP, 'Like up'),
        (LIKE_DOWN, 'Like Down'),
        (NO_LIKE, 'No Like'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activity = models.CharField(max_length=16, choices=LIKE_CHOICES, default=NO_LIKE)

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user_like',
                             related_query_name='user_likes',
                             help_text='User likes to the post')
    post = models.ForeignKey(Posts,
                             on_delete=models.CASCADE,
                             related_name='post_like',
                             related_query_name='post_likes',
                             help_text='Post being liked on')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = LikesManager()


class Comment(models.Model):
    """
    Comment model keeps track of post being liked or not
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_content = models.TextField(blank=False, null=False, help_text='Post content')
    comment_published = models.BooleanField(default=False)
    post = models.ForeignKey(Posts,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             related_query_name='comments',
                             help_text='Post being commented on')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CommentsManager()
