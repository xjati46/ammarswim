from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from coach_app.models import Coach
from student_app.models import Student


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nama User'
        self.fields['username'].help_text = ''
        self.fields['email'].label = 'Alamat E-Mail'
        self.fields['password1'].help_text = 'Minimal 8 karakter'
        self.fields['password2'].label = 'Konfirmasi Password'
        self.fields['password2'].help_text = 'Ketik ulang Password'


class CoachProfileForm(forms.ModelForm):
    class Meta:
        model = Coach
        exclude = ['user', 'bagi_hasil']


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']
