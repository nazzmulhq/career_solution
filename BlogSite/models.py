from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    question = models.TextField(max_length=264, verbose_name='Put a question')
    slug = models.SlugField(max_length=164, unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.question


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment


class Like(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='like_question')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='like_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')


class DisLike(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='dislike_question')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='disLike_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disLike_user')

