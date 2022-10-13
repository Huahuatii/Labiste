"""Labsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views,account
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.homepage),
    path('layout',views.layout),
    path('homepage',views.homepage),
    path('research',views.research),
    path('members',views.members),
    path('achievement',views.achievement),
    path('databases',views.databases),
    path('contact',views.contact),
    path('members/list',views.members_list),
    path('members/add',views.members_add),
    path('members/delete',views.members_delete),
    path('members/<int:nid>/edit',views.members_edit),
    path('test',views.test),
    path('achievement/list',views.achievement_list),
    path('articles/add',views.articles_add),
    path('achievement/<int:nid>/edit',views.achievement_edit),
    path('achievement/delete',views.achievement_delete),
    path('login',account.login),
    ] 
urlpatterns += staticfiles_urlpatterns()

