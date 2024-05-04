from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()
class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'username',
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'password'
    }))


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'rounded-0 my-0', 'style': 'border:none; border-bottom: 1px solid rgb(33, 37, 41)'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'rounded-0 my-0', 'style': 'border:none; border-bottom: 1px solid rgb(33, 37, 41)'}),
            'email': forms.EmailInput(
                attrs={'class': 'rounded-0 my-0', 'style': 'border:none; border-bottom: 1px solid rgb(33, 37, 41)'}),
            'password': forms.PasswordInput(
                attrs={'class': 'rounded-0 my-0', 'style': 'border:none; border-bottom: 1px solid rgb(33, 37, 41)'}),
        }
        help_texts = {
            'username': 'Letters, digits and @/./+/-/_ only.',
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError("Parollar bir xil emas !")
        return self.cleaned_data['confirm_password']