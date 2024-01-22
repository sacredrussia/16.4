from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'type', 'rating', 'title')
    list_filter = ('author',  'type', 'rating', 'title')
    search_fields = ('title', 'category__name')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
