# Generated by Django 5.1.1 on 2024-09-29 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("line_step", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="foodprocesslinestep",
            name="order",
        ),
    ]
