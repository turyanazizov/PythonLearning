from django.views.generic import TemplateView
from . models import *
class IndexTemplateView(TemplateView):
    template_name = 'index.html'

class CategoryTemplateView(TemplateView):
    template_name = 'category.html'

class ResultTemplateView(TemplateView):
    template_name = 'search-result.html'

class SingleTemplateView(TemplateView):
    template_name = 'single-post.html'
