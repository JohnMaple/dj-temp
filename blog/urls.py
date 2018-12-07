from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.index, name='index'),
]

