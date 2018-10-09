from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def total_tags():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html') 
def show_latest_post():
    latest_posts = Post.published.order_by('-publish')[:5]
    return {'latest_posts':latest_posts}  

@register.simple_tag()
def get_most_commented_posts():
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:5]    


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))