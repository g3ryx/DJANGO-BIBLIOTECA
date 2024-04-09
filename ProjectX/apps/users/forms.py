from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from .models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        label="Email",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email'
            }
        )
    )

    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '****'
            }
        )
    )

    def clean(self):
        self.cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return self.cleaned_data


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'nombre', 'apellido']

    def clean_password2(self):
        if self.cleaned_data.get('password') != self.cleaned_data['password2']:
            self.add_error('password2', 'Las password no coinciden.')
