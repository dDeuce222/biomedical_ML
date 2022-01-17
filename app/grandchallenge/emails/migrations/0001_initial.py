# Generated by Django 3.2.10 on 2022-01-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=1024)),
                (
                    "body",
                    models.TextField(
                        help_text="Email body will be prepended with 'Dear [username],' and will end with 'Kind regards, Grand Challenge team' and a link to unsubscribe from the mailing list."
                    ),
                ),
                ("sent", models.BooleanField(default=False)),
                ("sent_at", models.DateTimeField(blank=True, null=True)),
                (
                    "status_report",
                    models.JSONField(
                        blank=True,
                        default=None,
                        help_text="This stores the page number of the last successfully sent email batch for this email.",
                        null=True,
                    ),
                ),
            ],
        ),
    ]
