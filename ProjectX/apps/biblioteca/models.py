from django.db import models


class Autor(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Editorial(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tematica(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Libro(models.Model):
    title = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default=None)
    year_of_edition = models.IntegerField()
    tematica = models.ForeignKey(Tematica, on_delete=models.CASCADE, default=None)
    isbn = models.CharField(max_length=13)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, default=None)
    year_editorial = models.IntegerField(default="0")
    resumen = models.TextField()

    def __str__(self):
        return self.title
