# Generated by Django 3.1.13 on 2021-09-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("cases", "0003_auto_20210406_0753")]

    operations = [
        migrations.AddField(
            model_name="image",
            name="patient_age",
            field=models.CharField(blank=True, default="", max_length=4),
        ),
        migrations.AddField(
            model_name="image",
            name="patient_birth_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="image",
            name="patient_id",
            field=models.CharField(blank=True, default="", max_length=64),
        ),
        migrations.AddField(
            model_name="image",
            name="patient_name",
            field=models.CharField(blank=True, default="", max_length=324),
        ),
        migrations.AddField(
            model_name="image",
            name="patient_sex",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                default="",
                max_length=1,
            ),
        ),
        migrations.AddField(
            model_name="image",
            name="series_description",
            field=models.CharField(blank=True, default="", max_length=64),
        ),
        migrations.AddField(
            model_name="image",
            name="series_instance_uid",
            field=models.CharField(blank=True, default="", max_length=64),
        ),
        migrations.AddField(
            model_name="image",
            name="study_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="image",
            name="study_description",
            field=models.CharField(blank=True, default="", max_length=64),
        ),
        migrations.AddField(
            model_name="image",
            name="study_instance_uid",
            field=models.CharField(blank=True, default="", max_length=64),
        ),
    ]