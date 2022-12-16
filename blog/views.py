from django.shortcuts import render, get_object_or_404 # get_object_or_404 - позволяет найти объект под нужным номером
# либо отобразить 404
# ошибку
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date') # сортировка по дате
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id): # передаём не только запрос но и имя переменной (blog_id)
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
