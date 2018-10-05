from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_list(request):
  posts = Post.published.all()
  return render(request, "blog/post/list.html", 
                                            {'posts':posts})


def post_detail(request, year, month, day, post):
  post = get_object_or_404(Post, status='publish',
                                        publish__year=year,
                                        publish__month=month,
                                        publish__day=day,
                                        slug=post)
  return render(request, "blog/post/detail.html", 
                                                {'post':post})    
