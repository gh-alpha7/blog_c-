from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    post1=Post.objects.filter(title="Where to start from??")
    post2=Post.objects.filter(title="after implementations..")
    
    return render(request, 'blog/post_list.html', {'postss':posts})
