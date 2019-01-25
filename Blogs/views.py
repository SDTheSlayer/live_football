from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import models
from . import forms


def blog_list(request):
    blogs = models.Blog.objects.all()
    return render(request, 'Blogs/blog_list.html', {'blogs': blogs})


def blog_detail(request, pk):
    blog = models.Blog.objects.get(id=pk)
    comments = blog.comment_set.all()
    form = forms.commentform()
    if request.method == 'POST':
        form = forms.commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(blog.get_absolute_url())


    return render(request, 'Blogs/blog_detail.html', {'blog': blog, 'comments': comments ,'form': form})


# Create your views here.
