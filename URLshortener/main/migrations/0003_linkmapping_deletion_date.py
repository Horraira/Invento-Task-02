# Generated by Django 4.1.1 on 2022-09-07 02:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_linkmapping_delete_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="linkmapping",
            name="deletion_date",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
