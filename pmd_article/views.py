from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import markdown
# Create your views here.

def index(request):
    """
    主页，展示文章列表
    :param request:
    :return:
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
    :param request:
    :return:
    """
    article = ArticleInfo.objects.filter(id=id)[0]
    html = markdown.markdown(article.a_content)
    context = {
        'title': article.a_title,
        'article': article,
        'html': html
    }
    return render(request, 'pmd_article/detail.html', context)
