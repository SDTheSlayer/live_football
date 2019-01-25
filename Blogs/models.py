from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User



class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('Blogs:blogdetail', kwargs={'pk': self.id}, )


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
