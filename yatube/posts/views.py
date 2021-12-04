from django.shortcuts import render
from .models import Post


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date
    # по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def posts_friends(request):  # Create your views here.
    template = 'posts/posts_friends.html'
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)


def posts_all(request, anyslug):  # Create your views here.
    template = 'posts/posts_all.html'
    context = {
        'text': f"<p>{anyslug}</p>"
    }
    return render(request, template, context)
