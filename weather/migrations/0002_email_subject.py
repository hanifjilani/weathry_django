# Generated by Django 4.2.7 on 2024-02-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weather", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="email",
            name="subject",
            field=models.CharField(default="Default Subject", max_length=120),
            preserve_default=False,
        ),
    ]