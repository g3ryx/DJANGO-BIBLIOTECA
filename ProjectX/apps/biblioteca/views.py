from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from apps.users.helpers import *
from django.db.models import Q

class LibroUpdateView(StaffRequiredMixin, UpdateView):
    model = Libro
    template_name = "update.html"
    fields = [
        "title",
        "autor",
        "year_of_edition",
        "tematica",
        "isbn",
        "editorial",
        "year_editorial",
        "resumen"
    ]
    success_url = "/"
    login_url = reverse_lazy('users_app:user-login')

@login_required(login_url='/login/')
def create_view(request):
    context = {}
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "CrearLibro.html", context)

def list_view(request):
    context = {}
    query = request.GET.get('query')

    if query:
        query_parts = query.split()
        if len(query_parts) >= 2:
            libros = Libro.objects.filter(
                Q(title__icontains=query) |
                Q(autor__name__icontains=query) |
                Q(autor__surname__icontains=query) |
                Q(autor__name__icontains=query_parts[0]) & Q(autor__surname__icontains=query_parts[1]) |
                Q(tematica__name__icontains=query) |
                Q(isbn__icontains=query) |
                Q(editorial__name__icontains=query) |
                Q(year_of_edition__icontains=query) |
                Q(title__icontains=query[0]) |
                Q(title__icontains=query[:len(query) // 2]) |
                Q(autor__name__icontains=query[0]) |
                Q(autor__name__icontains=query[:len(query) // 2]) |
                Q(autor__surname__icontains=query[0]) |
                Q(autor__surname__icontains=query[:len(query) // 2]) |
                Q(tematica__name__icontains=query[0]) |
                Q(tematica__name__icontains=query[:len(query) // 2]) |
                Q(isbn__icontains=query[0]) |
                Q(isbn__icontains=query[:len(query) // 2]) |
                Q(editorial__name__icontains=query[0]) |
                Q(editorial__name__icontains=query[:len(query) // 2]) |
                Q(year_of_edition__icontains=query[0]) |
                Q(year_of_edition__icontains=query[:len(query) // 2])
            ).order_by('year_of_edition')
        else:
            libros = Libro.objects.filter(
                Q(title__icontains=query) |
                Q(autor__name__icontains=query) |
                Q(autor__surname__icontains=query) |
                Q(tematica__name__icontains=query) |
                Q(isbn__icontains=query) |
                Q(editorial__name__icontains=query) |
                Q(year_of_edition__icontains=query)
            ).order_by('year_of_edition')
        context['query'] = query
    else:
        libros = Libro.objects.all().order_by('year_of_edition')

    context['dataset'] = libros
    return render(request, "lista_libro.html", context)
