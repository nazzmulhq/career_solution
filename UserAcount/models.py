from django.contrib.auth.models import User
from django.db import models


class UserProfileInfoUpdate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile_info', primary_key=True)
    hobby = models.CharField(max_length=264)
    occupation = models.CharField(max_length=264)
    educational_institutions = models.CharField(max_length=264)
    subject_of_study = models.CharField(max_length=264)
    level = FRUIT_CHOICES = [
        ('নিম্ন মাধ্যমিক', 'নিম্ন মাধ্যমিক'),
        ('মাধ্যমিক', 'মাধ্যমিক'),
        ('উচ্চ মাধ্যমিক', 'উচ্চ মাধ্যমিক'),
        ('স্নাতক', 'স্নাতক'),
        ('স্নাতকোত্তর', 'স্নাতকোত্তর'),
        ('এম ফিল', 'এম ফিল'),
        ('পিএইচডি', 'পিএইচডি'),
    ]
    subject_of_level = models.CharField(choices=level, max_length=50)
    your_self = models.CharField(max_length=512)
    profile_pic = models.ImageField(upload_to='profile_pic/', verbose_name='Upload profile picture')

    def __str__(self):
        return str(self.user)
