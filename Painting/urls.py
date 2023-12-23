from django.contrib import admin
from django.urls import path 
from PaintingApp.views import PaintingApiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('painting/', PaintingApiView.as_view(), name='painting-list'),
    path('painting/<int:painting_ID>/', PaintingApiView.as_view(), name='paining-detail'),
]