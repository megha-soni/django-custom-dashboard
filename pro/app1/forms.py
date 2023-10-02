from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User

class Signup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

    def clean_first_name(self):
        first_name=self.cleaned_data['first_name']
        if len(first_name)<4:
            raise forms.ValidationError('name must be equal or greater than 4 char')
        return first_name
    def clean_email(self):
       email=self.cleaned_data['email']
       if len(email)<10:
            raise forms.ValidationError('email must equal or greater than 11 char')
       return email
    def clean_contact(self):
        contact=self.cleaned_data['contact']
        if len(contact)!=10:
            raise forms.ValidationError('contact must equal to 10 digit')
        return contact
    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError('password should be greater than 8')


class CustomUserForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        
class CustomAdminForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email','is_active','is_staff','is_superuser','groups','user_permissions','date_joined','last_login']
        
