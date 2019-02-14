# Generated by Django 2.1.4 on 2019-01-15 14:53

from django.db import migrations
from django.contrib.auth.models import User, Group
from django.conf import settings


def create_retina_import_user_forward(apps, schema_editor):
    # Create retina import user
    User.objects.create_user(settings.RETINA_IMPORT_USER_NAME)


def create_retina_import_user_backward(apps, schema_editor):
    # Remove retina import user
    User.objects.get(username=settings.RETINA_IMPORT_USER_NAME).delete()


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(
            create_retina_import_user_forward,
            create_retina_import_user_backward,
        )
    ]
