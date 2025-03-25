from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Content
# Create your views here.
from django.views.generic import TemplateView




class ContentList(ListView):
    def get_queryset(self):
        return Content.objects.filter(status=True)


class ContentDetail(DetailView):
    def get_object(self):
        return get_object_or_404(
            Content.objects.filter(status=True),
            pk=self.kwargs.get('pk'))



