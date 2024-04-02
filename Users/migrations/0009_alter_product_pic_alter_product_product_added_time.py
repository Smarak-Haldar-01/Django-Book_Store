# Generated by Django 5.0.3 on 2024-03-25 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0008_product_delete_product_carsoule"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="pic",
            field=models.FileField(
                max_length=250,
                upload_to="carsoul_product/<django.db.models.fields.CharField>",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_added_time",
            field=models.TimeField(
                default=datetime.datetime(2024, 3, 25, 17, 23, 22, 975932)
            ),
        ),
    ]
