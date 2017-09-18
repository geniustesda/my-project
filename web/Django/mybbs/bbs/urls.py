from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^category/(\d+)/$', views.category, name="category_detail"),
    url(r'article/(\d+)/$', views.article_detail, name='article_detail'),
]
