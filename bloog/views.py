from django.shortcuts import render, get_object_or_404
from bloog.models import Article


def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'bloog/post_details.html', {'article': article})


def blog(request):
    articles = Article.objects.published()
    return render(request, 'bloog/blog.html', {'articles': articles})
