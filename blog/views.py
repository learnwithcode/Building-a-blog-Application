from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailForm, CommentForm, SearchForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
# Create your views here.

class PostList(ListView):
  queryset = Post.published.all()
  template_name = 'blog/post/list.html'
  paginate_by = 1
  context_object_name = 'posts'

def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 2) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        #search
    form = SearchForm()
    query = None
    results = []
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['search']
            search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B') #default weights are D, C, B AND A refer to 0.1, 0.2, 0.4, and 1.0 respectively
            search_query = SearchQuery(query)
            results = Post.objects.annotate(search=search_vector,
                                            rank=SearchRank(search_vector, search_query)
                                            ).filter(rank__gte=0.3).order_by('-rank')
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts,
                   'tag':tag,
                   'form':form,
                    'query':query,
                    'results':results})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status='publish',
                                        publish__year=year,
                                        publish__month=month,
                                        publish__day=day,
                                        slug=post)
    #list of active comment  for the post
    comments = post.comments.filter(active=True)
    new_comment = None
    #list of similar  post
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_post = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_post = similar_post.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:5]      
    if request.method == 'POST':
        #A commen was posted
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #create comment object but don't save to databate yet
            new_comment = comment_form.save(commit=False)
            #Assign a current Post to the comment
            new_comment.post = post
            new_comment.save()
            
    else:
        comment_form = CommentForm()  

    return render(request, "blog/post/detail.html", 
                                                {'post':post,
                                                'comments':comments,
                                                'new_comment': new_comment,  
                                                'comment_form':comment_form,
                                                'similar_post':similar_post})    

def post_share(request,post_id):
    post = get_object_or_404(Post, status='publish', id=post_id)
    sent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # form field password validation
            cd = form.cleaned_data
            #send_mail...
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email']}) recommends you reading '{post.title}'"
            message = f"Read '{post.title}' at {post_url}\n\n{cd['name']}'s comments: {cd['message']}"
            send_mail(subject, message, cd['email'], [cd['to']])
            sent=True
    else:
        form = EmailForm()        
    return render(request, "blog/post/share.html", 
                                                {'form':form,
                                                'post':post})

                                                                              