# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from . import models


# Create your views here.
category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')


def index(request):
    print(category_list)
    category_obj = models.Category.objects.get(position_index=1)
    article_list = models.Article.objects.filter(status='published')
    return render(request, 'bbs/index.html', {"category_list": category_list,
                                              "category_obj": category_obj,
                                              "article_list": article_list},)
    # return HttpResponse("OK")


def category(request, id):  # id是URL配置中category/(\d+)/$的(\d+),一个括号就是一个参数
    category_obj = models.Category.objects.get(id=id)
    if category_obj.position_index == 1:
        article_list = models.Article.objects.filter(status='published')  # 把所有状态为“已发布”的查出来
    else:
        article_list = models.Article.objects.filter(category_id=category_obj.id, status='published')
    return render(request, "bbs/index.html", {'category_list': category_list,
                                              'category_obj': category_obj,
                                              'article_list': article_list, })


def article_detail(request, id):
        article_obj = models.Article.objects.get(id=id)
        return render(request, 'bbs/article_detail.html', {'article_obj': article_obj, 'category_list': category_list})

