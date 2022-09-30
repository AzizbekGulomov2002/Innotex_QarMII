from django.urls import path
from .views import PostListView, PostDetailView
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('jurnal_haqida', jurnal_haqida.as_view(), name='jurnal_haqida'),
    path('nizom', nizom.as_view(), name='nizom'),
    path('tahrir', tahrir.as_view(), name='tahrir'),
    path('biz', biz.as_view(), name='biz'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)