from django.urls import path, include

# from django.views.generic import TemplateView
from .views import index, suggestView, SearchView


urlpatterns = [
    path('', index, name='index'),
    path('suggest/', suggestView.as_view(), name='suggest'),
    path('search/', SearchView.as_view(), name='search')
]
