from django.views.generic import ListView, TemplateView
from .models import Post
from django.shortcuts import render


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class InputPageView(TemplateView):
    template_name = 'input.html'

