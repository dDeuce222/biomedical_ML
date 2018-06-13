# Generated by Django 2.0.6 on 2018-06-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_auto_20180613_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawimagefile',
            name='filename',
            field=models.CharField(default='asdf', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rawimagefile',
            name='staged_file_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
