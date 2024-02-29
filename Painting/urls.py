from django.contrib import admin
from django.urls import path , include
from PaintingApp.views import PaintingApiView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('painting/', PaintingApiView.as_view(), name='painting-list'),
    path('painting/<int:painting_ID>/', PaintingApiView.as_view(), name='paining-detail'),
    path('api/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)