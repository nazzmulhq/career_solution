"""Carisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blogsite/', include('blogsite.urls'))
"""
from django.urls import path
from BlogSite import views

app_name = 'BlogSite'

urlpatterns = [

    path('forum/', views.forum, name='forum'),
    path('forum/no_question_comment/', views.no_question_comment, name='no_comment'),
    path('forum/question_comment/', views.question_comment, name='comment'),
    path('details/<slug>/', views.blog_details, name='blog_details'),
    path('forum/like/<pk>/<id>/', views.like, name='like'),
    path('forum/dislike/<pk>/<id>/', views.dislike, name='dislike'),
    path('forum/comment/edit/<pk>/', views.comment_edit, name='comment_edit'),
    path('forum/comment/delete/<pk>/', views.comment_delete, name='comment_delete'),
    path('book/', views.book, name='book'),

]