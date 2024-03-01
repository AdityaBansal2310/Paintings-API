from django.contrib import admin
from django.contrib.auth.models import User
from .models import Painting


@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Title', 'Artist', 'Price')  # Customize displayed fields


def has_painting_permission(self, request, obj=None):
    return request.user.is_superuser or request.user.has_perm('app_name.can_create_painting')  # Replace 'app_name' with your app name


admin.site.has_perm = has_painting_permission
