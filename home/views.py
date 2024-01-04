from django.shortcuts import render
from bloog.models import Article
# from django.urls import reverse


def home(request):
    articles = Article.objects.published()
    print(Article.objects.count())
    recent_articles = Article.objects.published()[:3]
    # .order_by('-updated', '-created')
    # article = Article.objects.get(id=1)
    # article.myfile = bytes('salam amir', 'utf-8')
    return render(request, 'home/index.html', {'articles': articles, 'recent_articles': recent_articles})
