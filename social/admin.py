# Register your models here.

from django.contrib import admin

from .models import User, Address, Likes, Comment, Posts


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'gender', 'birth_date', 'contact_address')
    search_fields = ['id', 'email', 'first_name', 'last_name']


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'street', 'zip', 'city',)
    search_fields = ['id', 'zip', 'city', ]


class LikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity', 'user', 'post')
    search_fields = ['id', ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_content', 'comment_published', 'post')
    search_fields = ['id', ]


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'headline', 'content', 'author_email', 'published', 'category', 'like', 'author', 'created_at',
        'updated_at')
    search_fields = ['headline', 'content', 'author__id', 'author__email']

    @staticmethod
    def author_email(obj):
        return obj.author.email


admin.site.register(User, UserAdmin)
admin.site.register(Posts, PostAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Likes, LikesAdmin)
admin.site.register(Comment, CommentAdmin)
