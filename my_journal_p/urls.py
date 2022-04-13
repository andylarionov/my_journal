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
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    #Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Cтраница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),


]