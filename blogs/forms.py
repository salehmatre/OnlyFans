from django import forms
from CustomUsers.models import User


"""Форма для регистрации пользователя"""


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@example.com',
    }))
    username = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя',
    }))
    password = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))
    password2 = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль',
    }))

    def clean(self, password1=None, password2=None):
        if not self.cleaned_data['password'] == self.cleaned_data['password2'] or not self.cleaned_data['password2']:
            self._errors['password2'] = self.error_class(['Пароли не совпадают'])
        return self.cleaned_data

    def save(self, commit=True):
        return User.objects.create_user(email=self.cleaned_data['email'],
                username=self.cleaned_data['username'], password=self.cleaned_data['password'])

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')


"""Форма для логина пользователя"""


class LogInForm(forms.ModelForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@example.com',
    }))

    password = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))

    class Meta:
        model = User
        fields = ('email', 'password')