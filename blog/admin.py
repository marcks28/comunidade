from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    display_list = ['title', 'created_date', 'published_date']


admin.site.register(Post, PostAdmin)
