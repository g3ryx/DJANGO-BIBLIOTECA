from django.shortcuts import render
from .models import *

from django.views.generic import (
    TemplateView,
)

# Create your views here.

class ListPosts(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super(ListPosts, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()

        return context

class PostView(TemplateView):
    model = Post
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['images'] = ImagesPost.objects.filter()

        return context
