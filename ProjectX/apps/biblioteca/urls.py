from django.urls import path
from .views import *

app_name = 'biblioteca_app'

urlpatterns = [
    path('libro/<int:pk>/', LibroUpdateView.as_view(), name="libro-update"),
    path('create', create_view, name="create_view"),
    path('', list_view, name="list-libros")
]
