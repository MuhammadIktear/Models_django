
from django import views
from django.urls import path,include
from . import views
urlpatterns = [
    path('1',views.home),
]
