# Generated by Django 4.2 on 2024-10-27 01:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0007_order_link_sent"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]
