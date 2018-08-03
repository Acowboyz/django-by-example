from django.contrib import admin

from .models import Post
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


# register Post to admin page
admin.site.register(Post, PostAdmin)
