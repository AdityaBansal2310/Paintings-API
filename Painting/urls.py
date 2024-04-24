from django.contrib import admin
from django.urls import path , include
from PaintingApp.views import LikePaintingAPIView, PaintingApiView , CommentApiView,CommentDeleteAPIView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('painting/', PaintingApiView.as_view(), name='painting-list'),
    path('painting/<int:painting_ID>/', PaintingApiView.as_view(), name='paining-detail'),
    path('api/', include('accounts.urls')),
    path('painting/<int:painting_ID>/like/', LikePaintingAPIView.as_view(), name='like-painting'),
    path('painting/<int:painting_ID>/comment/', CommentApiView.as_view(), name='comment-painting'),
    path('painting/<int:painting_id>/comment/<int:comment_id>/', CommentDeleteAPIView.as_view(), name='comment-delete'),
    path('', RedirectView.as_view(url='/painting/'), name='root-redirect'),  # Redirect root URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)