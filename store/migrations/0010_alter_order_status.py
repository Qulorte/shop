# Generated by Django 4.2 on 2024-10-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0009_remove_order_completed_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Created"),
                    ("In progress", "In Progress"),
                    ("Completed", "Completed"),
                    ("Rejected", "Rejected"),
                ],
                default="created",
                max_length=255,
            ),
        ),
    ]
