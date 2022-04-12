"""Определяет схемы URL для пользователя"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    #Включить URL авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
]