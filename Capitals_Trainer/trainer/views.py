from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
	template_name = 'Capitals(2).html'
	

# Create your views here.
