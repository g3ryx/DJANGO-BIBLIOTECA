from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro

        fields = [
            "title",
            "autor",
            "year_of_edition",
            "isbn",
            "editorial",
            "year_editorial",
            "tematica",
            "resumen",
        ]


class BuscarLibroForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
