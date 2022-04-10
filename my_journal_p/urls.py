"""Определяет схемы URL для my_journal_p"""
from django.urls import path

from . import views

app_name = 'my_journal_p'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    #Страница со списками всех тем
    path('topics/', views.topics, name='topics'),
    #Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic')
]