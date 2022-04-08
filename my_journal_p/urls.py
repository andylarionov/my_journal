"""Определяет схемы URL для my_journal_p"""
from django.urls import path

from . import views

app_name = 'my_journal_p'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index')
]