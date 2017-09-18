# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError  # 这个就是Django admin后台当出错时,抛出的红色错误提示,要自定义错误时,就得引入此方法
from django.contrib.auth.models import User
from django.db import models
import datetime


# Create your models here.
# 论坛帖子表
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'标题')
    brief = models.CharField(null=True, blank=True, max_length=255, verbose_name=u'摘要')
    category = models.ForeignKey("Category", verbose_name=u'所属板块')  # 由于category在下方，所以用引号括起来，django会自动回调寻找
    content = models.TextField(verbose_name=u'文章内容')
    author = models.ForeignKey('UserProfile', verbose_name=u'作者')
    pub_date = models.DateField(blank=True, null=True, verbose_name=u'发布日期')
    last_modify = models.DateField(auto_now=True, verbose_name=u'修改时间')
    priority = models.IntegerField(default=1000, verbose_name=u'优先级')
    status_choice = (('draft', u'草稿'),
                     ('published', u'已发布'),
                     ('hidden', u'隐藏'),
                    )
    status = models.CharField(choices=status_choice, default='published', max_length=128, verbose_name=u'状态')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'帖子'
        verbose_name_plural = u'帖子'

    # django的model类在保存数据的时候，会默认调用self.clean()方法，所以可以在clean方法中定义数据的一些验证
    def clean(self):
        # 如果帖子有发布时间，就说明是发布过的帖子，发布过的帖子就不可以把状态改成草稿状态了
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(u'已发布的帖子，不能更改状态为草稿')
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()


# 用户评论表
class Comment(models.Model):
    article = models.ForeignKey('Article', verbose_name=u'所属文章')
    parent_comment = models.ForeignKey('self', related_name="my_children", blank=True, null=True, verbose_name=u'父评论')
    comment_choice = ((1, u'评论'),
                      (2, u'点赞'))
    comment_type = models.IntegerField(choices=comment_choice, default=1, verbose_name=u'评论类型')
    user = models.ForeignKey("UserProfile", verbose_name=u'评论人')
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = u'用户评论'
        verbose_name_plural = u'用户评论'

    # 这里有一个问题,这里我们设置了允许为空,那就意味着我们在页面上点了评论,却又没有输入内容,这样岂不是很不合理.那么怎么实现只要你点了评论,内容就不能为空.
    # 那么我们会问,为什么允许为空,直接不为空就好了.因为我们这里把评论和点赞放到了一张表中,当为点赞时,当然就不需要评论内容了.所以可以为空.
    # 我们会想在前端进行判断或者在views写代码进行判断,这里告诉你这里我们就可以实现这个限制.使用Django中clean()方法,models类在保存之前它会调用self.clean方法,所以我们可以在这里定义clean方法,进行验证
    def clean(self):
        # 如果comment状态为空，那么评论内容就不允许为空
        if self.comment_type == 1 and self.comment is None:
            raise ValidationError(u"评论内容不能为空")
            # 我想知道这个报错显示在什么位置,我们看到每一个字段有报错,也只是显示在form表单的字段上,这里做了判断错误信息会显示在什么地方?
            # 后面把错误信息显示的位置截图展示
    date = models.DateTimeField(auto_now_add=True, verbose_name=u'评论时间')


# 板块表
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=u'板块名称')  # unique是否唯一
    brief = models.CharField(null=True, blank=True, max_length=255, verbose_name=u'摘要')
    set_as_top_menu = models.BooleanField(default=False, verbose_name=u'是否将此板块设置在首页顶部')
    position_index = models.SmallIntegerField(verbose_name=u'顶部展示的位置')
    admins = models.ManyToManyField('UserProfile', blank=True, verbose_name=u'版主')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'板块分类'
        verbose_name_plural = u'板块分类'


# 用户表继承django里面的user
class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'关联django内部的用户')
    name = models.CharField(max_length=32, verbose_name=u'昵称')
    signature = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'签名')
    head_img = models.ImageField(height_field=None, width_field=None, blank=True, null=True, verbose_name=u'头像')
    # ImageFied字段说明https://docs.djangoproject.com/en/1.9/ref/models/fields/
    # 大概的意思是,ImageField 继承的是FileField,除了FileField的属性被继承了
    # 它还有两个属性 ImageField.height_field和ImageField.width_field
    # 设置后当你存入图片字段时,它会把默认尺寸设置成高height_field宽:width_field
    # 如果想在前端上传图像,需要下载一个Pillow模块,具体使用后面会用到

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'


# 用户组表
class UserGroup(models.Model):
    pass


