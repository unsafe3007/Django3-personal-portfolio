from django.shortcuts import render
from .models import Project  # импортируем модель проекта


def home(request):
    projects = Project.objects.all()  # получаем импорт всех данных (при помощи функции all() из базы данных)
    return render(request, 'portfolio/home.html', {'projects': projects})  # используя переменную projects передаём
    # словарь в шаблон где ключем будет projects


def about(request):
    return render(request, 'portfolio/about.html')
