from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def hello(request):
    return HttpResponse('Hello, world!')


def index(request):
    blog_list = models.Article.objects.all().order_by('-id')
    context = {
        'title': '博客首页',
        'blog_list': blog_list
    }
    return render(request, 'index/index.html', context)
