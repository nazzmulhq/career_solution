import django_filters
from django_filters import CharFilter, widgets

from .models import *


class UniversityFilter(django_filters.FilterSet):
    institutions = CharFilter(field_name='institutions', lookup_expr='icontains')

    class Meta:
        model = University
        fields = ['types','location', 'category', 'institutions_category', 'institutions']


class BranchesFilter(django_filters.FilterSet):
    class Meta:
        model = Branches
        fields = ['subjects_category', 'branches_name', 'study_level']

