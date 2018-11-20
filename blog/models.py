from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.

class PublishedManager(models.Manager):
  def get_queryset(self):
    return super(PublishedManager, self).get_queryset().filter(status='publish')

class Post(models.Model):
  STATUS_CHOICES = (
    ('draft','DRAFT'),
    ('publish','PUBLISH')
  )
  title = models.CharField(max_length=250)
  image = models.ImageField(upload_to='blog_posts/%y/%m/%d', blank=True)
  author = models.ForeignKey(User, 
                            on_delete=models.CASCADE,
                            related_name='blog_posts')
  slug = models.SlugField(max_length=250,
                                        unique_for_date='publish')
  # body = models.TextField()   
  body = RichTextUploadingField(external_plugin_resources=[('youtube', '/static/vendors/ckeditor_plugins/youtube/', 'plugin.js',)])                                  
  publish = models.DateTimeField(default=timezone.now)
  created =  models.DateTimeField(auto_now_add=True)
  updated =  models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=250,
                                        choices=STATUS_CHOICES, 
                                        default='draft')                                   


  objects = models.Manager() 
  published = PublishedManager() 
  tags = TaggableManager()  
  
  class Meta:
    ordering = ('-publish',) 

  def __str__(self):
    return self.title                                     

  def get_absolute_url(self):
    return reverse('blog:post_detail', args=[
                                              self.publish.year,
                                              self.publish.month,
                                              self.publish.day,
                                              self.slug,])


class Comment(models.Model):
  post =  models.ForeignKey(Post, 
                                  on_delete=models.CASCADE,
                                  related_name='comments') 
  name = models.CharField(max_length=80)
  email = models.EmailField()
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  class Meta:
    ordering= ('-created',)

  def __str__(self):
    return f'Comment by {self.name} on {self.post}'                                                                               