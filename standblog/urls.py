from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('articles/', include('bloog.urls')),
    # path('static/', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
