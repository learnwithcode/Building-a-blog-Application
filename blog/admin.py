from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'publish', 'status', 'created', 'updated']
  list_filter = ['created', 'updated', 'publish']
  search_fields = ['title', 'body']
  prepopulated_fields = {'slug':('title',)}
  raw_id_fields = ('author',)
  date_hierarchy = 'publish'
  ordering = ['publish', 'status']
