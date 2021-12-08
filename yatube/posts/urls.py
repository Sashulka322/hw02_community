from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Посты
    path('group/', views.group_posts, name='group_posts'),
    # Пост
    path('group/<slug:anyslug>/', views.posts_detail, name='group_detali'),

]
