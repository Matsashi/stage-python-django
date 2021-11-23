from django.contrib import admin
from blog.models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    search_fields = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'created_on')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
