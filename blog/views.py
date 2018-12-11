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


def orm(request):
    """
    数据库api操作
    :param request:
    :return:
    """
    # 第一种：增加一篇文章
    # models.Article.objects.create(title='新增文章标题2', category_id=1, body='新增内容2', user_id=1)

    # 第二种：添加数据，实例化表类，在实例化里传参为字段和值
    # obj = models.Article(title='新增文章标题2', category_id=1, body='新增内容2', user_id=1)
    # obj.save()

    # 第三种：将要写入的数据组合成字典，键为字段值为数据（推荐）
    # dic = {'title': '新增文章标题3', 'category_id': '1', 'body': '新增内容3', 'user_id': '1'}
    # models.Article.objects.create(**dic)

    # 删除数据
    # title = models.Article.objects.filter(id=7).delete()
    # print(title)

    # 修改数据
    # title = models.Article.objects.filter(id=6).update(title='被修改了')
    # print(title)

    # 查询数据
    # all() 获取所有数据
    article_list = models.Article.objects.all()
    print(article_list)

    # filter(**kwargs) 筛选查询的数据
    article_list = models.Article.objects.filter(id__gt=2)
    print(article_list)
    article_list = models.Article.objects.filter(id__in=[2])
    print(article_list)

    # get() 查询单一对象
    article = models.Article.objects.get(pk=2)
    print(article)

    # exclude() 查询不匹配条件的对象
    article_list = models.Article.objects.exclude(id__in=[2])
    print(article_list)

    # values() 返回字典对象
    article_list = models.Article.objects.exclude(id__in=[2]).values()
    print(article_list)

    # values_list() 返回元组
    article_list = models.Article.objects.exclude(id__in=[2]).values_list('id', 'title')
    print(article_list)

    # reverse() 反向排序
    article_list = models.Article.objects.reverse()
    print(article_list)
    print(models.Article.objects.all())
    print(models.Article.objects.count())   # 返回记录数

    return HttpResponse('orm')
