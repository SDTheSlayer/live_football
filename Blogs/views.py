



from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import models


def blog_list(request):
    blogs = models.Blog.objects.all()
    return render(request, 'Blogs/blog_list.html', {'blogs': blogs})




# Create your views here.
