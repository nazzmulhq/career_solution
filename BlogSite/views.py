from django.shortcuts import render, redirect
from BlogSite.models import Question, Comment, Like, DisLike
from BlogSite.forms import CommentForms, QuestionForms
from BlogSite.filters import QuestionFilter
from django.contrib.auth.decorators import login_required
import uuid


# Create your views here.

@login_required()
def forum(request):
    comment_form = CommentForms()
    question = Question.objects.all()
    question_filter = QuestionFilter()
    form = QuestionForms()
    if 'filter_question' in request.POST:
        if request.method == 'POST':
            question_filter = QuestionFilter(request.POST, queryset=question)
            question = question_filter.qs
            if question_filter.is_valid():
                data = {
                    'questions': question,
                    'form': form,
                    'comment_form': comment_form,
                    'question_filter': question_filter
                }
                return render(request, 'blogsite/forum1.html', context=data)
    if request.method == 'POST':
        form = QuestionForms(request.POST)
        if form.is_valid():
            question_obj = form.save(commit=False)
            question_obj.author = request.user
            slug_set = question_obj.question
            question_obj.slug = slug_set.replace(" ", "-") + "-" + str(uuid.uuid1())
            question_obj.save()
            return redirect('/blogsite/forum/')

    data = {
        'questions': question,
        'form': form,
        'comment_form': comment_form,
        'question_filter': question_filter
    }
    return render(request, 'blogsite/forum1.html', context=data)


@login_required()
def no_question_comment(request):
    if request.method == 'GET':
        question = Question.objects.all()
        questions = []
        for x in question:
            comment = Comment.objects.filter(question_id=x.id)
            if len(comment) == 0:
                questions.append(x)
        data = {
            'questions': questions,
            'form': QuestionForms(),
            'question_filter': QuestionFilter(),
            'comment_form': CommentForms()
        }
        return render(request, 'blogsite/no_comment.html', context=data)
    if 'filter_question' in request.POST:
        if request.method == 'POST':
            question = Question.objects.all()
            question_filter = QuestionFilter(request.POST, queryset=question)
            question = question_filter.qs

            if question_filter.is_valid():
                data = {
                    'questions': question,
                    'form': QuestionForms(),
                    'question_filter': question_filter,
                    'comment_form': CommentForms()
                }
                return render(request, 'blogsite/forum1.html', context=data)

    if request.method == 'POST':
        form = QuestionForms(request.POST)
        if form.is_valid():
            question_obj = form.save(commit=False)
            question_obj.author = request.user
            slug_set = question_obj.question
            question_obj.slug = slug_set.replace(" ", "-") + "-" + str(uuid.uuid1())
            question_obj.save()
            return redirect('/blogsite/forum/')


@login_required()
def question_comment(request):
    if request.method == 'GET':
        question = Question.objects.all()
        questions = []
        for x in question:
            comment = Comment.objects.filter(question_id=x.id)
            if len(comment) != 0:
                questions.append(x)
        data = {
            'questions': questions,
            'form': QuestionForms(),
            'question_filter': QuestionFilter(),
            'comment_form': CommentForms()
        }
        return render(request, 'blogsite/comment.html', context=data)

    if 'filter_question' in request.POST:
        if request.method == 'POST':
            question = Question.objects.all()
            question_filter = QuestionFilter(request.POST, queryset=question)
            question = question_filter.qs

            if question_filter.is_valid():
                data = {
                    'questions': question,
                    'form': QuestionForms(),
                    'question_filter': question_filter
                }
                return render(request, 'blogsite/forum1.html', context=data)

    if request.method == 'POST':
        form = QuestionForms(request.POST)
        if form.is_valid():
            question_obj = form.save(commit=False)
            question_obj.author = request.user
            slug_set = question_obj.question
            question_obj.slug = slug_set.replace(" ", "-") + "-" + str(uuid.uuid1())
            question_obj.save()
            return redirect('/blogsite/forum/')


@login_required()
def blog_details(request, slug):
    question = Question.objects.get(slug=slug)
    comment_form = CommentForms()
    if request.method == 'POST':
        comment_form = CommentForms(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.question = question
            comment.save()
            return redirect('/blogsite/forum/')

    data = {
        'questions': question,
        'form': QuestionForms(),
        'comment_form': comment_form
    }
    return render(request, 'blogsite/forum1.html', context=data)


@login_required()
def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment_form = CommentForms(instance=comment)
    if request.method == 'POST':
        comment_form = CommentForms(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('/blogsite/forum/')
    data = {
        'questions': Question.objects.all(),
        'comment_form': comment_form,
        'comment_pk': comment.pk
    }
    return render(request, 'blogsite/forum1.html', context=data)


@login_required()
def comment_delete(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('/blogsite/forum/')


@login_required()
def like(request, pk, id):
    question = Question.objects.get(id=id)
    comment = Comment.objects.get(pk=pk)
    user = request.user
    already_like = Like.objects.filter(question=question, comment=comment, user=user)
    if not already_like:
        like_post = Like(question=question, comment=comment, user=user)
        like_post.save()
    return redirect('/blogsite/forum/')


@login_required()
def dislike(request, pk, id):
    question = Question.objects.get(id=id)
    comment = Comment.objects.get(pk=pk)
    user = request.user
    already_like = DisLike.objects.filter(question=question, comment=comment, user=user)
    if not already_like:
        dislike_post = DisLike(question=question, comment=comment, user=user)
        dislike_post.save()
    return redirect('/blogsite/forum/')


@login_required()
def book(request):
    return render(request, 'blogsite/book.html')
