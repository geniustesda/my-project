# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
# Register your models here.
from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'pub_date', 'last_modify', 'status')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'parent_comment', 'comment_type', 'comment', 'user')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'set_as_top_menu', 'position_index',)


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.UserProfile)
