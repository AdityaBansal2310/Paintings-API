from django.db import migrations
from django.contrib.auth.models import User, Permission

def assign_permissions(apps, schema_editor):
    admin_user = User.objects.get(username='TriptiBansal')  # Replace 'admin' with your superuser's username
    can_create_painting = Permission.objects.get(codename='can_create_painting')
    can_edit_painting = Permission.objects.get(codename='can_edit_painting')
    can_delete_painting = Permission.objects.get(codename='can_delete_painting')
    
    admin_user.user_permissions.add(can_create_painting, can_edit_painting, can_delete_painting)

class Migration(migrations.Migration):

    dependencies = [
        ('PaintingApp', '0002_remove_painting_image_url_painting_image_and_more'),  # Adjust the dependency based on your project
    ]

    operations = [
        migrations.RunPython(assign_permissions),
    ]
