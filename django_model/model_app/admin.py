from django.contrib import admin

# Register your models here.
from .import models
admin.site.register(models.Student)

from model_app.models import StudentModel
admin.site.register(StudentModel)