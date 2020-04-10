from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'publish'
    list_display = ('title', 'slug', 'author', 'created', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    ordering = ('-publish', 'status')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    search_fields = ('title', 'body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
