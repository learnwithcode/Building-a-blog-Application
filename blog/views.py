from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class PostList(ListView):
  queryset = Post.published.all()
  template_name = 'blog/post/list.html'
  paginate_by = 1
  context_object_name = 'posts'

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 1) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, year, month, day, post):
  post = get_object_or_404(Post, status='publish',
                                        publish__year=year,
                                        publish__month=month,
                                        publish__day=day,
                                        slug=post)
  return render(request, "blog/post/detail.html", 
                                                {'post':post})    
