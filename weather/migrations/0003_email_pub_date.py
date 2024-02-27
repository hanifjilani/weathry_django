# Generated by Django 4.2.7 on 2024-02-16 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weather", "0002_email_subject"),
    ]

    operations = [
        migrations.AddField(
            model_name="email",
            name="pub_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 16, 12, 44, 5, 947427, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date published",
            ),
            preserve_default=False,
        ),
    ]