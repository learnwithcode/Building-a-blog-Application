from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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
  body = models.TextField()                                      
  publish = models.DateTimeField(default=timezone.now)
  created =  models.DateTimeField(auto_now_add=True)
  updated =  models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=250,
                                        choices=STATUS_CHOICES, 
                                        default='draft')                                   


  objects = models.Manager() 
  published = PublishedManager()   
  
  class Meta:
    ordering = ('-publish',) 

  def __str__(self):
    return self.title                                     
