from django.contrib import admin
from .models import Post, Comment
# Register your models here.

admin.site.site_header = 'blogen'
admin.site.site_title = 'blogen'
admin.site.index_title = 'site administration'
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'publish', 'status', 'created', 'updated']
  list_filter = ['created', 'updated', 'publish']
  search_fields = ['title', 'body']
  prepopulated_fields = {'slug':('title',)}
  raw_id_fields = ('author',)
  date_hierarchy = 'publish'
  ordering = ['-publish', 'status']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'post', 'created', 'updated')
  list_filter = ('active', 'updated', 'created')
  search_fields = ('name', 'email', 'body')