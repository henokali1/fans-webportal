from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')
    gender = forms.CharField(max_length=10, label='Gender', widget=forms.TextInput(attrs={'class': "gender-autocomplete"}))
    id_number = forms.CharField(max_length=10, label='ID Number')
    department = forms.CharField(max_length=50, label='Department', widget=forms.TextInput(attrs={'class': "department-autocomplete"}))
    job_title = forms.CharField(max_length=50, label="Job Title", widget=forms.TextInput(attrs={'class': "job-title-autocomplete"}))


    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.gender = self.cleaned_data['gender']
        user.id_number = self.cleaned_data['id_number']
        user.department = self.cleaned_data['department']
        user.job_title = self.cleaned_data['job_title']
        user.save()
        return user