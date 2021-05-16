from django.db import models
from django.conf import settings
from django.utils import timezone
    
class My_Library(models.Model):
    Books = models.CharField(max_length=200, verbose_name= 'Книга')
    Author = models.CharField(max_length=200, verbose_name= 'Автор')
    Genre = models.CharField(max_length=200, verbose_name= 'Жанр')
    data = models.DateField( verbose_name= 'Дата')
    coments = models.CharField(max_length=300, verbose_name= 'Коментарии')

    def __str__(self):
        return self.Books

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        


    
   
    

