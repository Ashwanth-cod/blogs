from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog/', blog_list, name='blog_list'),
    path('blog/create/', blog_create, name='blog_create'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
