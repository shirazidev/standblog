from django.shortcuts import render, get_object_or_404
from bloog.models import Article


def post_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    return render(request, 'bloog/post_details.html', {'article': article})
