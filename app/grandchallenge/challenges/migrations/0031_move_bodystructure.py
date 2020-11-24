# Generated by Django 3.1.1 on 2020-11-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anatomy", "0002_bodystructure"),
        ("challenges", "0030_move_bodyregion"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name="challenge",
                    name="structures",
                    field=models.ManyToManyField(
                        blank=True,
                        help_text="What structures are used in this challenge?",
                        to="anatomy.BodyStructure",
                    ),
                ),
                migrations.AlterField(
                    model_name="externalchallenge",
                    name="structures",
                    field=models.ManyToManyField(
                        blank=True,
                        help_text="What structures are used in this challenge?",
                        to="anatomy.BodyStructure",
                    ),
                ),
            ],
            # Reusing an existing table
            database_operations=[],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[migrations.DeleteModel(name="BodyStructure")],
            database_operations=[
                migrations.AlterModelTable(
                    name="BodyStructure", table="anatomy_bodystructure",
                )
            ],
        ),
    ]