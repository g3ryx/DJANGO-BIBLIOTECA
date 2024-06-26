# Generated by Django 5.0.1 on 2024-02-08 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('nacionality', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'editoriales',
            },
        ),
        migrations.CreateModel(
            name='Tematica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'tematicas',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year_of_edition', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=255)),
                ('resumen', models.CharField(max_length=255)),
                ('autor', models.ManyToManyField(related_name='libros', to='biblioteca.autor')),
                ('editorial', models.ManyToManyField(related_name='libros', to='biblioteca.editorial')),
                ('tematica', models.ManyToManyField(related_name='libros', to='biblioteca.tematica')),
            ],
            options={
                'verbose_name_plural': 'libros',
            },
        ),
    ]
