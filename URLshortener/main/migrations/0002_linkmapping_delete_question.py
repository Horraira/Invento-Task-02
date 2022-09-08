# Generated by Django 4.1.1 on 2022-09-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LinkMapping",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("original_url", models.CharField(max_length=256)),
                ("hash", models.CharField(db_index=True, max_length=10, unique=True)),
                ("creation_date", models.DateTimeField(verbose_name="creation date")),
            ],
        ),
        migrations.DeleteModel(name="Question",),
    ]