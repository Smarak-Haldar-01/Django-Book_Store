# Generated by Django 5.0.3 on 2024-03-25 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0016_alter_product_product_added_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_code",
            field=models.IntegerField(default=101086),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_added_time",
            field=models.TimeField(
                default=datetime.datetime(2024, 3, 26, 0, 50, 8, 588392)
            ),
        ),
    ]