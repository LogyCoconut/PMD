from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from .models import *
import markdown
import datetime
import time
# Create your views here.


def index(request):
    """
    主页，展示文章列表
    """
    article_list = ArticleInfo.objects.all().order_by("-id")
    # 过滤掉ｉｄ＝３的文章
    article_list = article_list.filter(~Q(id=3))
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
    # 接受post
    post = request.POST
    title = post.get('title')
    content = post.get('article')

    # 当id=3时，新建文章
    if id == "3":
        # 获取当前日期
        time_stamp = time.time()
        now_time = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d')
        # 创建新的记录
        dic = {
            'a_title': title,
            'a_content': content,
            'a_ct_time': now_time,
        }
        ArticleInfo.objects.create(**dic)
        # 找到最新的那条记录
        iid = str(ArticleInfo.objects.last().id)
    else:
        # 修改数据库
        article = ArticleInfo.objects.filter(id=id)[0]
        article.a_title = title
        article.a_content = content
        article.save()
        iid = id
        print("al")

    return redirect("/w/"+iid)

def delete(request, id):
    """
    删除文章
    """
    ArticleInfo.objects.filter(id=id).delete()
    return redirect("/")