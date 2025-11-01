from django.urls import path

from .views import HomePageView 

urlpatterns = [

    path('Hom', HomePageView.as_view(), name='Hom'),

    ]
