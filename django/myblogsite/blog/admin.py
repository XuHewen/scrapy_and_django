from django.contrib import admin
from .models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    search_fields = ('title', 'body', )


class CommentAdmin(admin.ModelAdmin):
    pass

    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)