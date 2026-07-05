from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'view_count')
    list_filter = ('is_published',)
    search_fields = ('title',)
