from django.shortcuts import render
from WebSite.models import *
from WebSite.filters import UniversityFilter, BranchesFilter
from django.http import JsonResponse


# Create your views here.
class BranchesAndStudy:
    university = University.objects.all()
    brc_name = {}
    study_level = {}
    for x in university:
        br_name = BranchesName.objects.filter(branches_branchesname__university_id=x.id).distinct()
        study_lv = StudyLevel.objects.filter(branches__university=x.id).distinct()
        dict1 = {x.id: br_name}
        dict2 = {x.id: study_lv}
        brc_name.update(dict1)
        study_level.update(dict2)


class AllValue:
    university = University.objects.all()
    location = Location.objects.all()
    types = Types.objects.all()
    category = Category.objects.all()
    institutionsCategory = InstitutionsCategory.objects.all()
    studyLevel = StudyLevel.objects.all()
    subjectsCategory = SubjectsCategory.objects.all()
    branches = Branches.objects.all()
    branches_name = BranchesName.objects.all()
    universityfilter = UniversityFilter()
    Branchesfilter = BranchesFilter()
    data = {
        'all': university,
        'location': location,
        'types': types,
        'category': category,
        'institutionsCategory': institutionsCategory,
        'studyLevel': studyLevel,
        'subjectsCategory': subjectsCategory,
        'branches': branches,
        'branches_name': branches_name,
        'brc_name': BranchesAndStudy.brc_name,
        'study_level': BranchesAndStudy.study_level,
        'universityfilter': universityfilter,
        'BranchesFilter': Branchesfilter

    }


def index(request):
    return render(request, 'website/index.html', context={
        'all_university': University.objects.all(),
        'all_course':SubjectsCategory.objects.all()
    })


def about(request):
    return render(request, 'website/about.html')


def career(request):
    return render(request, 'website/career.html')


def junior_predict(request):
    return render(request, 'website/predict.html')


def science(request):
    return render(request, 'website/science.html')


def arts(request):
    return render(request, 'website/arts.html')


def commerce(request):
    return render(request, 'website/commerce.html')


def careerguides(request):
    return render(request, 'website/careerguides.html')

def computer(request):
    return render(request, 'website/computer.html')


def institution(request):
    if request.method == "GET":
        return render(request, 'website/institution_filter.html', context=AllValue.data)
    elif request.method == "POST":
        university = AllValue.university
        universityfilter = UniversityFilter(request.POST, queryset=university)
        university = universityfilter.qs
        data = {
            'all': university,
            'location': AllValue.location,
            'types': AllValue.types,
            'category': AllValue.category,
            'institutionsCategory': AllValue.institutionsCategory,
            'studyLevel': AllValue.studyLevel,
            'subjectsCategory': AllValue.subjectsCategory,
            'branches': AllValue.branches,
            'branches_name': AllValue.branches_name,
            'brc_name': BranchesAndStudy.brc_name,
            'study_level': BranchesAndStudy.study_level,
            'universityfilter': AllValue.universityfilter

        }

        return render(request, 'website/institution_filter.html', context=data)


def filters(request, types):
    if types == 1:
        public = University.objects.filter(types=types)
        data = {
            'all': public,
            'location': AllValue.location,
            'types': AllValue.types,
            'category': AllValue.category,
            'institutionsCategory': AllValue.institutionsCategory,
            'studyLevel': AllValue.studyLevel,
            'subjectsCategory': AllValue.subjectsCategory,
            'branches': AllValue.branches,
            'branches_name': AllValue.branches_name,
            'brc_name': BranchesAndStudy.brc_name,
            'study_level': BranchesAndStudy.study_level,
            'universityfilter': AllValue.universityfilter
        }
        if request.method == "POST":
            university = AllValue.university
            universityfilter = UniversityFilter(request.POST, queryset=university)
            university = universityfilter.qs
            data = {
                'all': university,
                'location': AllValue.location,
                'types': AllValue.types,
                'category': AllValue.category,
                'institutionsCategory': AllValue.institutionsCategory,
                'studyLevel': AllValue.studyLevel,
                'subjectsCategory': AllValue.subjectsCategory,
                'brc_name': BranchesAndStudy.brc_name,
                'study_level': BranchesAndStudy.study_level,
                'universityfilter': AllValue.universityfilter
            }
            return render(request, 'website/institution_filter.html', context=data)
        return render(request, 'website/institution_filter.html', context=data)
    elif types == 2:
        private = University.objects.filter(types=types)
        data = {
            'all': private,
            'location': AllValue.location,
            'types': AllValue.types,
            'category': AllValue.category,
            'institutionsCategory': AllValue.institutionsCategory,
            'studyLevel': AllValue.studyLevel,
            'subjectsCategory': AllValue.subjectsCategory,
            'brc_name': BranchesAndStudy.brc_name,
            'study_level': BranchesAndStudy.study_level,
            'universityfilter': AllValue.universityfilter
        }
        if request.method == "POST":
            university = AllValue.university
            universityfilter = UniversityFilter(request.POST, queryset=university)
            university = universityfilter.qs
            data = {
                'all': university,
                'location': AllValue.location,
                'types': AllValue.types,
                'category': AllValue.category,
                'institutionsCategory': AllValue.institutionsCategory,
                'studyLevel': AllValue.studyLevel,
                'subjectsCategory': AllValue.subjectsCategory,
                'brc_name': BranchesAndStudy.brc_name,
                'study_level': BranchesAndStudy.study_level,
                'universityfilter': AllValue.universityfilter
            }
            return render(request, 'website/institution_filter.html', context=data)
        return render(request, 'website/institution_filter.html', context=data)


def courses(request):
    if request.method == "GET":
        info = {}
        for x in AllValue.subjectsCategory:
            branches_name = BranchesName.objects.filter(branches_branchesname__subjects_category=x.id).distinct()
            branches_dic = {x.id: branches_name}
            info.update(branches_dic)

        data = {
            'all': AllValue.university,
            'location': AllValue.location,
            'types': AllValue.types,
            'category': AllValue.category,
            'institutionsCategory': AllValue.institutionsCategory,
            'studyLevel': AllValue.studyLevel,
            'subjectsCategory': AllValue.subjectsCategory,
            'branches': AllValue.branches,
            'branches_name': info

        }
        return render(request, 'website/courses.html', context=data)

    return render(request, 'website/courses.html')


def courses_details_filters(request, id):
    university = University.objects.filter(branches_university=id).distinct()
    brc_name = BranchesName.objects.filter(id=id).distinct()
    boln = True
    study_level = {}
    for x in university:
        study_lv = StudyLevel.objects.filter(branches__university_id=x.id).distinct()
        dict2 = {x.id: study_lv}
        study_level.update(dict2)
    data = {
        'all': Branches.objects.filter(branches_name_id=id),
        'location': AllValue.location,
        'types': AllValue.types,
        'category': AllValue.category,
        'institutionsCategory': AllValue.institutionsCategory,
        'studyLevel': AllValue.studyLevel,
        'subjectsCategory': AllValue.subjectsCategory,
        'branches': AllValue.branches,
        'branches_name': AllValue.branches_name,
        'brc_name': brc_name,
        'study_level': BranchesAndStudy.study_level,
        'boln': boln,
        'BranchesFilter': AllValue.Branchesfilter
    }

    return render(request, 'website/directory.html', context=data)


def directory(request):
    if request.method == "GET":
        Branchesfilter = BranchesFilter()
        data = {
            'all': Branches.objects.all(),
            'location': AllValue.location,
            'types': AllValue.types,
            'category': AllValue.category,
            'institutionsCategory': AllValue.institutionsCategory,
            'studyLevel': AllValue.studyLevel,
            'subjectsCategory': AllValue.subjectsCategory,
            'branches': AllValue.branches,
            'branches_name': AllValue.branches_name,
            'brc_name': BranchesAndStudy.brc_name,
            'study_level': BranchesAndStudy.study_level,
            'BranchesFilter': Branchesfilter
        }

        return render(request, 'website/directory.html', context=data)
    elif request.method == "POST":
        branches = AllValue.branches
        branchesfilter = BranchesFilter(request.POST, queryset=branches)
        branches = branchesfilter.qs

        data = {
            'all': branches,
            'location': AllValue.location,
            'types': AllValue.types,
            'category': AllValue.category,
            'institutionsCategory': AllValue.institutionsCategory,
            'studyLevel': AllValue.studyLevel,
            'subjectsCategory': AllValue.subjectsCategory,
            'branches': AllValue.branches,
            'branches_name': AllValue.branches_name,
            'brc_name': BranchesAndStudy.brc_name,
            'study_level': BranchesAndStudy.study_level,
            'BranchesFilter': AllValue.Branchesfilter

        }
        if request.is_ajax() and request.method == 'POST':
            subject_category = request.POST['subjects_category_id']
            branches_name = BranchesName.objects.filter(
                branches_branchesname__subjects_category_id=subject_category).values()
            print(branches_name)

            return JsonResponse({
                'state': 1,
                'branches_names': list(branches_name)
            })

        return render(request, 'website/directory.html', context=data)
