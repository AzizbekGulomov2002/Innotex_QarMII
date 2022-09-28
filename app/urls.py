from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from app.views import post_detail
urlpatterns = [
    path('', main),
    path('detail/<int:pk>/', post_detail.as_view(), name='post_detail'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)