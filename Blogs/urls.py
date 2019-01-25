from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    url(r'^$', views.blog_list , name='bloglist'),
    url(r'(?P<pk>\d+)/$', views.blog_detail, name='blogdetail'),
]
