from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User



class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        reverse()


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
