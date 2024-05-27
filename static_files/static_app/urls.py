from django.urls import path
from . import views

urlpatterns = [
    path('link/', views.link, name='link'),  # Root path for home view
    path('dummy/', views.dummy, name='dummy'),  # Path for dummy view
    path('form/', views.form, name='form'),  # Path for fprm view
    path('djangoForm/',views.djangoForm,name='djangoForm'),
    path('loginForm/',views.loginForm,name='loginForm'),
]
