from django.contrib import admin
from .models import My_Library 

class My_LibraryAdmin (admin.ModelAdmin):
    list_display = ("id", 'Books', 'Author', 'Genre', 'data', 'coments',)
    search_fields = ('Books', 'Author')
admin.site.register(My_Library, My_LibraryAdmin)
# Register your models here.
