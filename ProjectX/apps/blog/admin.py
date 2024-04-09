from django.contrib import admin
from .models import *

# Register your models here.
class ImagesPostAdmin(admin.StackedInline):
    model = ImagesPost

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
        inlines = [ImagesPostAdmin]

        class Meta:
            model = Post