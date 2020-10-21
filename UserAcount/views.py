from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from BlogSite.models import Question, Comment, Like, DisLike
from BlogSite.forms import QuestionForms, CommentForms
from .forms import UserForm, UserProfileUpdateForm, UserProfileInfoFrom
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import UserProfileInfoUpdate


def sign_up(request):
    User_Info = UserForm()
    register = False
    if request.method == "GET":
        return render(request, 'useracount/log_in.html', context={'User_Info': User_Info, 'register': register})

    if request.method == 'POST':
        User_Info = UserForm(data=request.POST)
        if User_Info.is_valid():
            userinfo = User_Info.save()
            userinfo.set_password(userinfo.password)
            userinfo.save()
            register = True
        return render(request, 'useracount/log_in.html', context={'User_Info': User_Info, 'register': register})


def log_in(request):
    User_Info = UserForm()
    if request.method == 'GET':
        return render(request, 'useracount/log_in.html', context={'User_Info': User_Info})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('WebSite:home'))
            else:
                return render(request, 'useracount/log_in.html', context={'massage_active': 'User not active!!'})
        else:
            return render(request, 'useracount/log_in.html', {'massage_login': 'Username and Password is not match!!'})


@login_required()
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('log_in'))


@login_required()
def my_profile(request):
    question = Question.objects.filter(author_id=request.user.id)
    return render(request, 'useracount/my_profile.html',
                  context={'questions': question, 'comment_form': CommentForms()})


@login_required()
def my_profile_edit(request):
    user_form = UserProfileUpdateForm(instance=request.user)
    profile_form = UserProfileInfoFrom()
    if request.method == 'POST':
        user_form = UserProfileUpdateForm(data=request.POST, instance=request.user)
        profile_form = UserProfileInfoFrom(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user_form = UserProfileUpdateForm(instance=request.user)
            profile_form = UserProfileInfoFrom(instance=request.user.user_profile_info)
    return render(request, 'useracount/my_profile_edit.html',
                  context={'user_form': user_form, 'profile_form': profile_form})


@login_required()
def like(request, pk, id):
    question = Question.objects.get(id=id)
    comment = Comment.objects.get(pk=pk)
    user = request.user
    already_like = Like.objects.filter(question=question, comment=comment, user=user)
    if not already_like:
        like_post = Like(question=question, comment=comment, user=user)
        like_post.save()
    return redirect('/account/profile/')


@login_required()
def dislike(request, pk, id):
    question = Question.objects.get(id=id)
    comment = Comment.objects.get(pk=pk)
    user = request.user
    already_like = DisLike.objects.filter(question=question, comment=comment, user=user)
    if not already_like:
        dislike_post = DisLike(question=question, comment=comment, user=user)
        dislike_post.save()
    return redirect('/account/profile/')


@login_required()
def comments(request, slug):
    question = Question.objects.get(slug=slug)
    comment_form = CommentForms()
    if request.method == 'POST':
        comment_form = CommentForms(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.question = question
            comment.save()
            return redirect('/account/profile/')

    data = {
        'questions': question,
        'form': QuestionForms(),
        'comment_form': comment_form
    }
    return render(request, 'useracount/my_profile.html', context=data)


@login_required()
def my_comment(request):
    question = Question.objects.filter(question_comment__user_id=request.user.id).distinct()
    return render(request, 'useracount/my_comment.html',
                  context={'questions': question, 'form': QuestionForms(), 'comment_form': CommentForms()})


@login_required()
def question_edit(request, slug):
    show_form = slug
    question = Question.objects.get(slug=slug)
    form = QuestionForms(instance=question)
    if request.method == 'POST':
        form = QuestionForms(data=request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('/account/profile/')
    data = {
        'questions': Question.objects.filter(author_id=request.user.id),
        'show_form': show_form,
        'form': form
    }
    return render(request, 'useracount/my_profile.html', context=data)


@login_required()
def question_delete(request, slug):
    question = Question.objects.get(slug=slug)
    question.delete()
    return redirect('/account/profile/')


@login_required()
def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    form = CommentForms(instance=comment)
    if request.method == 'POST':
        form = CommentForms(data=request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/account/profile/')
    data = {
        'questions': Question.objects.filter(author_id=request.user.id),
        'comment_form': form,
        'comment_pk': comment.pk
    }
    return render(request, 'useracount/my_profile.html', context=data)


@login_required()
def comment_delete(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('/account/profile/')
