# Generated by Django 5.1.1 on 2024-09-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("line", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="foodprocessline",
            name="bom",
            field=models.PositiveSmallIntegerField(default=0, verbose_name="bom"),
        ),
    ]
