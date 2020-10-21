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
from UserAcount import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('profile/', views.my_profile, name='account_profile'),
    path('profile/comments/<slug>/', views.comments, name='comments'),
    path('profile/edit/', views.my_profile_edit, name='account_profile_edit'),

    path('profile/like/<pk>/<id>/', views.like, name='like'),
    path('profile/dislike/<pk>/<id>/', views.dislike, name='dislike'),

    path('profile/my_comment/', views.my_comment, name='my_comment'),

    path('profile/question/edit/<slug>/', views.question_edit, name='question_edit'),
    path('profile/question/delete/<slug>/', views.question_delete, name='question_delete'),

    path('profile/comment/edit/<pk>/', views.comment_edit, name='profile_comment_edit'),
    path('profile/comment/delete/<pk>/', views.comment_delete, name='profile_comment_delete'),



]
