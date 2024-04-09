from django.contrib import admin
from .models import Autor, Editorial, Tematica, Libro

admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Tematica)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'year_of_edition', 'tematica', 'isbn', 'editorial', 'year_editorial')
    list_filter = ('year_of_edition', 'tematica', 'year_editorial', 'editorial')
    search_fields = ('title', 'autor__name', 'autor__surname', 'isbn')
    ordering = ('year_of_edition',)
