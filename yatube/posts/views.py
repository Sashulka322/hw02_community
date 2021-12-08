from django.shortcuts import render
from .models import Post


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date
    # по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Это главная страница Ya'
    # В словаре context отправляем информацию в шаблон
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request):  # Create your views here.
    template = 'posts/group_list.html'
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, context, template)


def posts_detail(request, anyslug):  # Create your views here.
    template = 'posts/posts_detail.html'
    context = {
        'text': f"<p>{anyslug}</p>"
    }
    return render(request, template, context)
