from django.shortcuts import render

from django.views.generic import TemplateView

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'
