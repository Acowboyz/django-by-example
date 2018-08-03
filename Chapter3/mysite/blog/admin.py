from django.contrib import admin

from .models import Post, Comment


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # display attributes in admin page
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # filter list
    list_filter = ('status', 'created', 'publish', 'author')
    # search by *
    search_fields = ('title', 'body')
    # autocomplete for the slug
    prepopulated_fields = {'slug': ('title',)}
    #
    raw_id_fields = ('author',)
    #
    date_hierarchy = 'publish'
    # default ordering
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    # display attributes in admin page
    list_display = ['name', 'email', 'post', 'created', 'active']
    # filter list
    list_filter = ('active', 'created', 'updated')
    # search by *
    search_fields = ('name', 'email', 'body')


# register Post to admin page
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
