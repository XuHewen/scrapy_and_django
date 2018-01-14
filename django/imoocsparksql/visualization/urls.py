from django.urls import path
# from django.views.generic import TemplateView
from .views import index, ajax_data


urlpatterns = [
    path('index/', index, name='index'),
    path('index/data/<day>/', ajax_data, name='ajax_data')
]