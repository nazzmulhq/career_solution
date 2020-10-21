import django_filters
from django import forms
from django_filters import CharFilter, widgets
from BlogSite.models import Question


class QuestionFilter(django_filters.FilterSet):
    question = CharFilter(field_name='question', lookup_expr='icontains',
                              widget=forms.DateInput(
                                  attrs={'class': "form-control border-0 bg-light",
                                         'placeholder': "Carisor -এ প্রশ্ন খুঁজুন...... ",
                                         'aria - describedby': "button-addon1"
                                         }
                              )
                              )

    class Meta:
        model = Question
        fields = ['question']