# Generated by Django 3.1.13 on 2021-10-14 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("studies", "0003_delete_study"),
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="Patient",),
    ]
