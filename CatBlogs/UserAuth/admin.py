from django.contrib import admin
from .models import CustomUser, Article, Comment, Like
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    list_display = ('email','username','is_staff', 'is_active')
admin.site.register(CustomUser, UserAdminConfig)

class ArticleAdmin(admin.ModelAdmin):  
    list_display = ('title', 'author','num_views', 'num_likes', 'date_published') 
admin.site.register(Article, ArticleAdmin)

class LikeTable(admin.ModelAdmin):  
    list_display = ( 'user','article', 'timestamp') 
admin.site.register(Like, LikeTable)

class CommentTable(admin.ModelAdmin):
    list_display = ('user', 'article', 'content')
admin.site.register(Comment, CommentTable)

