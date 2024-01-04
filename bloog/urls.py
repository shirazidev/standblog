from django.urls import path
from . import views
from bloog import views

app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>', views.post_detail, name='article_detail'),
    path('all/', views.blog, name='post'),
]