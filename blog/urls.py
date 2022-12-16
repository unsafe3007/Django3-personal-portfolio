from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail') # '<int:blog_id>/' принимает любой входящий запрос в urls.py
    # приложения blog, в котором содержится цифровое значение (int), далее запрос реализуется на функцию detail в
    # файле views.py где задаётся переменая blog_id и далее запрос идёт в detail.html
]