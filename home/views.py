from django.shortcuts import render
from bloog.models import Article

def home(request):
    articles = Article.objects.all()
    # article = Article.objects.get(id=1)
    # article.myfile = bytes('salam amir', 'utf-8')
    return render(request, 'home/index.html', {'articles': articles})
