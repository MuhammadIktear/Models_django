from email.mime import application
from django import forms
from django.core import validators
class contactFrom(forms.Form):
    name= forms.CharField(
        label="Full name",
        widget=forms.TextInput(attrs={
            'class': 'form-control p-2',
            'placeholder': 'Enter your name'
        }),
            validators=[
            validators.MaxLengthValidator(10, message='Enter a name with at most 10 characters'),
            validators.MinLengthValidator(5, message='Enter a name with at least 5 characters')
        ]
    )
    email = forms.EmailField(
        label="Email address",
        min_length=10,
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'form-control p-2',
            'placeholder': 'Enter your email'
        })
    )
    file = forms.FileField(
        label="Upload file",
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file p-2'
        }),
                    validators=[
            validators.FileExtensionValidator(allowed_extensions=['pdf'])
            ]
    )
    check= forms.BooleanField()
    age = forms.IntegerField(        
            label="Age",
            widget=forms.NumberInput(attrs={
            'class': 'form-control p-2',
            'placeholder': 'Enter your age'
        }),
            validators=[
            validators.MaxValueValidator(34, message='Age must be maximum 34y'),
            validators.MinValueValidator(18, message='Age must be minimum 18y')
                    ]
    )
    weight=forms.FloatField()
    birthday=forms.DateField(
        label="Birthday",
        widget=forms.DateInput(attrs={
            'class': 'form-control p-2',
            'placeholder': 'Select date of birth',
            'type': 'date'
        })
    )
    
    appoinment=forms.DateTimeField(
        label="Appointment date time",
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control p-2',
            'placeholder': 'Select date and time of your appointment',
            'type': 'datetime-local'  
        })

    )
    check= forms.BooleanField()
    CHOICES=[('s','small'),('m','medium'),('l','large')]
    size=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    Pizza=forms.MultipleChoiceField(choices=[('p','pepperoni'),('m','mashroom'),('b','beef')], widget=forms.CheckboxSelectMultiple)
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     age = cleaned_data.get('age')
    #     email = cleaned_data.get('email')
        
    #     if age is not None and age < 18:
    #         self.add_error('age',"You are a child yet")
        
    #     if email and not email.endswith('.com'):
    #         self.add_error('email', "Your email must contain '.com'.")
    #     return cleaned_data
