from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailForm, CommentForm
from django.core.mail import send_mail
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
    #list of active comment  for the post
    comments = post.comments.filter(active=True)
    new_comment = None
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
                                                'comment_form':comment_form})    

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
            send_mail(subject, message, 'pundirabhiraj@gmail.com', [cd['to']])
            sent=True
    else:
        form = EmailForm()        
    return render(request, "blog/post/share.html", 
                                                {'form':form,
                                                'post':post})