from django.urls import path
from .views import IndexTemplateView,SingleTemplateView,ResultTemplateView,CategoryTemplateView

app_name = 'home'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='home'),
    path('single/', SingleTemplateView.as_view(), name='single'),
    path('search/', ResultTemplateView.as_view(), name='search'),
    path('category/', CategoryTemplateView.as_view(), name='category'),
]