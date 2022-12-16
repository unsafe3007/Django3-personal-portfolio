#!!! Здесь можно задавать перечень моделей которые будут отображаться в панели администратора.
from django.contrib import admin
from .models import Project

#Регистрируем модели которые хотим видеть в админке
admin.site.register(Project)
