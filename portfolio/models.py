from django.db import models

"""
Создаём свою модель для представления портфолио. В скобках унаследуем класс от models. Мы создаём класс представляющий 
модель и обеспечивающий взаимодействие с БД Django. Модель необходима для создания таблицы и добавления в нее данных.
Когда мы что-либо добавляем или меняем в models.py - это называется миграцией (migrations)
"""
class Project(models.Model):
    title = models.CharField(max_length=100) # Указываем тип строки в терминах БД (CharField и в скобках настройки
                                             # отображения данного типа)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True) # blank=True - откр. страницу в новой вкладке браузера

    def __str__(self):
        return self.title