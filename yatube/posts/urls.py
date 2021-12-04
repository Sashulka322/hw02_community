from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('group/', views.posts_friends, name='posts_friends'),
    # Группа
    path('group/<slug:anyslug>/', views.posts_all, name='posts_all'),
]
