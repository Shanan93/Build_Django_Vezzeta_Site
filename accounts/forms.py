from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationForms(UserCreationForm):
        username = forms.CharField(label='اسم المستخدم ')
        first_name = forms.CharField(label = 'الاسم الاول')
        last_name = forms.CharField(label = 'الاسم الاخير')
        email = forms.EmailField(label = 'البريد الالكتروني')
        password1 = forms.CharField(label='كلمة المرور ', widget=forms.PasswordInput(), min_length=8)
        password2 = forms.CharField(label='تأكيد كلمة المرور  ', widget=forms.PasswordInput(), min_length=8)


        class Meta:
            model = User
            fields = ('username', 'password1','first_name','last_name','email','password2' )




class Login_Form(forms.ModelForm):
    username = forms.CharField(label='الاسم ')
    password = forms.CharField(label='كلمة المرور ', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'password' )





class UpdateUserForm(forms.ModelForm):

    first_name = forms.CharField(label = 'الاسم الاول')
    last_name = forms.CharField(label = 'الاسم الاخير')
    email = forms.EmailField(label = 'البريد الالكتروني')


    class Meta:
        model = User
        fields = ('first_name','last_name','email')
