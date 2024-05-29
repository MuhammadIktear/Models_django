from dataclasses import fields
from django import forms
from django.core import validators
from model_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel 
        fields='__all__'
        labels={
            'name':'Student Name',
            'father_name':'Father''s Name'
            
        }
        widgets={
            'name':forms.TextInput(attrs={
            'class': 'form-control p-2',
            'placeholder': 'Enter your name'
            }),
            'father_name':forms.TextInput(attrs={
            'class': 'form-control p-2',
            'placeholder': 'Enter your name'
            })        
        }
        
            
        