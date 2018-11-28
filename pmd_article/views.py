from django.shortcuts import render, redirect
from django.db.models import Q
from . import login_check
from .models import *
import markdown
import datetime
import time


def index(request):
    """
    主页，展示文章列表
    """
    article_list = ArticleInfo.objects.all().order_by("-id")
    # 过滤掉作为默认页的13
    article_list = article_list.filter(~Q(id=13))

    # 统计文章数和总字数
    article_count = len(article_list)
    word_count = 0
    for a in article_list:
        word_count += int(a.a_word_count)

    context ={
        'title': '椰子呆呆 - PMD',
        'article_list': article_list,
        'article_count': article_count,
        'word_count': word_count,
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


@login_check.login_auth
def write(request, id):
    """
    编辑界面
    """
    # 如果是默认编辑页则传入一个False
    is_default = False
    if id == "13":
        is_default = True

    article = ArticleInfo.objects.filter(id=id)[0]
    html = markdown.markdown(article.a_content)
    context = {
        'article': article,
        'html': html,
        'is_default': is_default,
    }
    return render(request, 'pmd_article/write.html', context)


def save(request, id):
    """
    修改文章或者新建文章
    """
    # 接受post
    post = request.POST
    title = post.get('title')
    content = post.get('article')

    # 当id=13时，新建文章
    if id == "13":
        # 获取当前日期
        time_stamp = time.time()
        now_time = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d')
        # 创建新的记录
        dic = {
            'a_title': title,
            'a_content': content,
            'a_ct_time': now_time,
            'a_word_count': count(content),
        }
        ArticleInfo.objects.create(**dic)
        # 找到最新的那条记录
        iid = str(ArticleInfo.objects.last().id)
    else:
        # 修改数据库
        article = ArticleInfo.objects.filter(id=id)[0]
        article.a_title = title
        article.a_content = content
        article.a_word_count = count(content)
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


def login(request):
    """
    登录界面
    """
    return render(request, "pmd_article/login.html")

def login_deal(request):
    """
    登陆处理，设置cookie
    """
    response = redirect('/')
    response.set_cookie('user', 'myself')
    return response


def count(txt):
    """
    统计字数
    """
    count = 0
    for s in txt:
        # 中文字符范围
        if '\u4e00' <= s <= '\u9fff':
            count += 1

    return count

