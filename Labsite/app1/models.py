from operator import mod
from re import T
from statistics import mode
from tkinter.tix import Tree
from unicodedata import category
from unittest import mock
from django.db import models

# Create your models here.

class members(models.Model):
    '''成员信息'''
    name = models.CharField(verbose_name='姓名', max_length=64, null=True)

    gender_choices = ((1, '男'), (2, '女'))
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices, null=True)

    phonenumber = models.CharField(verbose_name="电话",max_length=16,null=True)

    # native_place = models.CharField(verbose_name='籍贯', max_length=64, null=True,default='浙江杭州')
    age = models.IntegerField(verbose_name='年龄', null=True,default=18)
    description = models.CharField(verbose_name='个人描述', max_length=256, null=True,default='货拉拉拉不拉拉布拉多',blank=True)

    birthday = models.DateTimeField(verbose_name='生日', default='2022-9-1', null=True)
    
    email = models.CharField(verbose_name='邮箱', max_length=64, null=True,default='caiji88@zju.edu.cn',blank=True)

    # QQ = models.CharField(verbose_name='QQ', max_length=16, null=True)
    create_time = models.IntegerField(verbose_name='入学年份', default=2022, null=True)

    degree_choice=((1,'硕士一年级'),(2,'硕士二年级'),(3,'硕士三年级'),(4,'博士一年级'),(5,'博士二年级'),(6,'博士三年级'),(7,'博士四年级'),(8,'博士五年级'),(9,"毕业生"),(10,'博后'),(11,'其他'))

    grade = models.SmallIntegerField(verbose_name='年级', choices=degree_choice, null=True)
    # img = models.ImageField(verbose_name='个人照片[大小要求: <10M][像素要求: 1080×1080]', max_length=1000,
    #                         upload_to='media', null=True, blank=True)
    # img_src = models.CharField(verbose_name='确认照片名称', max_length=256, default='AW.jpg')
    shortname = models.CharField(verbose_name='姓名缩写[例如: HHT]', max_length=16, null=True)

    y_id = models.CharField(verbose_name='XX级XX',max_length=32,null=True,blank=True)   


class articles(models.Model):
    '''文献信息'''
    cat_class_choices = ((1,'论文'),(2,'代表性论文'),(3,'专利'),(4,'奖项'),(5,'其他'))
    cat_class = models.SmallIntegerField(verbose_name='类型',choices=cat_class_choices,null=True,default=1)
    name = models.CharField(verbose_name='文献标题',max_length=256,null=True)
    
    autor = models.CharField(verbose_name='作者',max_length=256,null=True)
    journal = models.CharField(verbose_name="期刊信息",max_length=256,null=True,default="Nat Commun. 2020 Mar")
    birthday = models.DateTimeField(verbose_name='发布时间', default='2022-9-1', null=True)
    href = models.CharField(verbose_name="文献链接",max_length=1024,null=True)
    abstract = models.TextField(verbose_name='摘要(50个单词以内，仅代表论文)',max_length=1024,null=True,blank=True)
    short_name = models.CharField(verbose_name='图片名称(仅代表论文)',max_length=64,default='CDK12.jpg',null=True)
    doi = models.CharField(verbose_name="doi(暂时不需要填)",max_length=256,null=True,blank=True)

    ifr = models.FloatField(verbose_name="影响因子",max_length=32,null=True,blank=True)

class admin(models.Model):
    admin = models.CharField(verbose_name='管理员',max_length=64,null=False)
    password = models.CharField(verbose_name="密码",max_length=64,null=False)