from django.urls import path
from .views import ContactTemplateView
app_name = 'contact'

urlpatterns = [
    path('', ContactTemplateView.as_view(), name='contact'),
]