from django.urls import path
from . import views

urlpatterns = [
    path('link/', views.link, name='link'),  # Root path for home view
    path('dummy/', views.dummy, name='dummy'),  # Path for dummy view
]
