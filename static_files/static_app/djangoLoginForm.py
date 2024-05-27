from email.mime import application
from django import forms
from django.core import validators

class DjangoLoginForm(forms.Form):
    password = forms.CharField(
        label='Password',
        min_length=5,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control p-2',
            'placeholder': 'Enter a password'
        }),
        validators=[
            validators.MaxLengthValidator(20, message='Enter a password with at most 20 characters'),
            validators.MinLengthValidator(5, message='Enter a password with at least 5 characters')
        ]
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control p-2',
            'placeholder': 'Enter confirm password'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', "Confirm password doesn't match")

        return cleaned_data