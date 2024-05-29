from django.urls import path

from model_app.views import student
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('delete/<int:roll>',views.delStudent,name='delStudent'),
    path('form/',student,name='student'),
]