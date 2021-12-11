from django.shortcuts import render, get_object_or_404
from .models import Post, Group

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
def group_posts(request, slug):  # Create your views here.
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by_('-pub_date')[:10]
    # template = 'posts/group_list.html'
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube',
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def posts_detail(request, anyslug):  # Create your views here.
    template = 'posts/posts_detail.html'
    context = {
        'text': f"<p>{anyslug}</p>"
    }
    return render(request, template, context)
