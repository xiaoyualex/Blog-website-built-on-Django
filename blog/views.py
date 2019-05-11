from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator

from . import models
# Create your views here.

def index(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    articles = models.Article.objects.all()

    paginator = Paginator(articles,3)
    page_num = paginator.num_pages
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    return render(request,'blog/index.html',
                  {
                      "articles": page_article_list,
                      "page_num": range(1, page_num + 1),
                      "curr_page": page,
                      "next_page": next_page,
                      "previous_page": previous_page
                  })

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    section_list = article.content.split('\n')
    return render(request,'blog/article_page.html',
                  {
                      'article':article,
                      'section_list':section_list
                  }
                  )

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})

def edit_action(request):
    title = request.POST.get('title','TITLE')
    subtitle = request.POST.get('subtitle','SUBTITLE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id','0')
    if article_id == '0':
        models.Article.objects.create(title=title,content=content,subtitle=subtitle)
        page = request.GET.get('page')
        if page:
            page = int(page)
        else:
            page = 1

        articles = models.Article.objects.all()
        paginator = Paginator(articles, 3)
        page_num = paginator.num_pages
        page_article_list = paginator.page(page)
        if page_article_list.has_next():
            next_page = page + 1
        else:
            next_page = page
        if page_article_list.has_previous():
            previous_page = page - 1
        else:
            previous_page = page

        return render(request, 'blog/index.html',
                      {
                          "articles": page_article_list,
                          "page_num": range(1, page_num + 1),
                          "curr_page": page,
                          "next_page": next_page,
                          "previous_page": previous_page
                      })

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.subtitle = subtitle
    article.save()
    section_list = article.content.split('\n')
    return render(request,'blog/article_page.html',
                  {
                      'article':article,
                      'section_list': section_list
                  })

def delete_article(request,article_id):
    models.Article.objects.filter(id=article_id).delete()
    return render(request,'blog/delete_article.html')

def about(request):
    return render(request,'blog/about.html')