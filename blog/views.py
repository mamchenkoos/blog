from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView
from .models import Post


@method_decorator(login_required, name='dispatch')
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 4


@method_decorator(login_required, name='dispatch')
class AboutPageView(TemplateView):
    template_name = 'about.html'


@method_decorator(login_required, name='dispatch')
class ImputPageView(TemplateView):
    template_name = 'imput.html'
