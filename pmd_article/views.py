from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import markdown
# Create your views here.


def index(request):
    """
    主页，展示文章列表
    """
    article_list = ArticleInfo.objects.all().order_by("-id")
    # introduction = article_list
    context ={
        'title': '椰子呆呆 - PMD',
        'article_list': article_list,
    }
    return render(request, 'pmd_article/index.html', context)


def detail(request, id):
    """
    文章的详情页
    """
    article = ArticleInfo.objects.filter(id=id)[0]
    html = markdown.markdown(article.a_content)
    context = {
        'title': article.a_title,
        'article': article,
        'html': html
    }
    return render(request, 'pmd_article/detail.html', context)


def write(request, id):
    """
    id=0: 新增文章
    id=其他: 修改文章
    """
    if id == 0:
        article = ArticleInfo.objects.filter(id=id)[0]
        html = markdown.markdown(article.a_content)
    else:
        article = ArticleInfo.objects.filter(id=id)[0]
        html = markdown.markdown(article.a_content)
    context = {
        'article': article,
        'html': html,
    }
    return render(request, 'pmd_article/write.html', context)


def save(request, id):
    """
    修改文章
    """
    txt = request.POST['article']
    txt = markdown.markdown(txt)
    data = {
        'data': txt,
    }
    return JsonResponse(data)