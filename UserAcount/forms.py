from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfoUpdate


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "form-control",
                                                 'placeholder': "প্রথম নাম*",

                                                 'id': 'first_name',
                                                 'required': "required",
                                                 'onfocus': "this.placeholder=''",
                                                 'onblur': "this.placeholder='প্রথম নাম*'",
                                                 }),

            'last_name': forms.TextInput(attrs={'class': "form-control",
                                                'placeholder': "শেষ নাম*",

                                                'id': 'last_name',
                                                'required': "required",
                                                'onfocus': "this.placeholder=''",
                                                'onblur': "this.placeholder='শেষ নাম*'",
                                                }),
            'username': forms.TextInput(attrs={'class': "form-control",
                                            'placeholder': "সম্পূর্ণ নাম*",

                                            'id': 'username',
                                            'required': "required",
                                            'onfocus': "this.placeholder=''",
                                            'onblur': "this.placeholder='সম্পূর্ণ নাম*'",
                                            }),
            'email': forms.TextInput(attrs={'class': "form-control",
                                            'placeholder': "ইমেইল*",

                                            'id': 'mail',
                                            'required': "required",
                                            'onfocus': "this.placeholder=''",
                                            'onblur': "this.placeholder='ইমেইল*'",
                                            })

        }


class UserProfileInfoFrom(forms.ModelForm):
    class Meta:
        model = UserProfileInfoUpdate
        fields = ['hobby', 'occupation', 'educational_institutions', 'subject_of_study', 'subject_of_level',
                  'your_self', 'profile_pic']
        widgets = {

            'hobby': forms.TextInput(attrs={'class': "form-control",
                                            'placeholder': "শখ*",

                                            'id': 'mail',
                                            'required': "required",
                                            'onfocus': "this.placeholder=''",
                                            'onblur': "this.placeholder='শখ*'",
                                            }),
            'occupation': forms.TextInput(attrs={'class': "form-control",
                                                 'placeholder': "পেশা*",

                                                 'id': 'occupation',
                                                 'required': "required",
                                                 'onfocus': "this.placeholder=''",
                                                 'onblur': "this.placeholder='পেশা*'",
                                                 }),
            'educational_institutions': forms.TextInput(attrs={'class': "form-control",
                                                               'placeholder': "শিক্ষাপ্রতিষ্ঠান*",

                                                               'id': 'educational_institutions',
                                                               'required': "required",
                                                               'onfocus': "this.placeholder=''",
                                                               'onblur': "this.placeholder='শিক্ষাপ্রতিষ্ঠান*'",
                                                               }),
            'subject_of_study': forms.TextInput(attrs={'class': "form-control",
                                                       'placeholder': "অধ্যায়নের বিষয়*",

                                                       'id': 'subject_of_study',
                                                       'required': "required",
                                                       'onfocus': "this.placeholder=''",
                                                       'onblur': "this.placeholder='অধ্যায়নের বিষয়*'",
                                                       }),
            'subject_of_level': forms.Select(attrs={'class': "form-control",
                                                    'placeholder': "অধ্যায়নের বিষয়*",

                                                    'id': 'subject_of_level',
                                                    'required': "required",
                                                    'onfocus': "this.placeholder=''",
                                                    'onblur': "this.placeholder='অধ্যায়নের বিষয়*'",
                                                    }),
            'your_self': forms.Textarea(attrs={'class': "form-control",
                                               'placeholder': "িজের সম্পর্কে লিখুন",

                                               'id': 'your_self',
                                               'required': "required",
                                               'onfocus': "this.placeholder=''",
                                               'onblur': "this.placeholder='িজের সম্পর্কে লিখুন*'",
                                               }),

        }
