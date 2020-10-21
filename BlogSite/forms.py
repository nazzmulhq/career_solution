from django import forms
from BlogSite.models import Comment, Question


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': "form-control",
                                             'placeholder': "Write..",
                                             'cols': "60",
                                             'rows': "5",
                                             'required': "required",
                                             'onfocus': "this.placeholder=''",
                                             'onblur': "this.placeholder='Comment*'",
                                             })

        }


class QuestionForms(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={'class': "form-control",
                                             'placeholder': "Write..",
                                             'cols': "60",
                                             'rows': "5",
                                             'id': 'name',
                                             'required': "required",
                                             'onfocus': "this.placeholder=''",
                                             'onblur': "this.placeholder='Write a question*'",
                                             })

        }
