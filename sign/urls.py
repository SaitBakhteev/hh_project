from django.urls import path
from .views import hh

urlpatterns = [path('', hh, name='main')]