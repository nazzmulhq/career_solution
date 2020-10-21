from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location


class Types(models.Model):
    types = models.CharField(max_length=50)

    def __str__(self):
        return self.types


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class InstitutionsCategory(models.Model):
    institutions_category = models.CharField(max_length=50)

    def __str__(self):
        return self.institutions_category


class University(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='university_location')
    types = models.ForeignKey(Types, on_delete=models.CASCADE, related_name='university_types')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='university_category')
    institutions_category = models.ForeignKey(InstitutionsCategory, on_delete=models.CASCADE,
                                          related_name='university_institutionscategory')
    institutions = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="university_icon/")
    website = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.institutions


class StudyLevel(models.Model):
    study_level_name = models.CharField(max_length=100)

    def __str__(self):
        return self.study_level_name


class Degree(models.Model):
    degree_name = models.CharField(max_length=100)

    def __str__(self):
        return self.degree_name


class SubjectsCategory(models.Model):
    subjects_category = models.CharField(max_length=100)

    def __str__(self):
        return self.subjects_category


class BranchesName(models.Model):
    branches_name = models.CharField(max_length=200)

    def __str__(self):
        return self.branches_name


class Branches(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='branches_university')
    subjects_category = models.ForeignKey(SubjectsCategory, on_delete=models.CASCADE,
                                          related_name='branches_institutionscategory')
    branches_name = models.ForeignKey(BranchesName, on_delete=models.CASCADE, related_name='branches_branchesname')
    study_level = models.ManyToManyField(StudyLevel)
    degree = models.ManyToManyField(Degree)

    def __str__(self):
        return str(self.university) +" ( "+str(self.branches_name) +")"
