# Generated by Django 5.0.3 on 2024-03-25 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0006_product_carsoule_pic2_product_carsoule_pic3_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product_carsoule",
            name="pic",
            field=models.FileField(
                max_length=250, upload_to="carsoul_product/{{name}}"
            ),
        ),
        migrations.AlterField(
            model_name="product_carsoule",
            name="pic2",
            field=models.FileField(
                max_length=250, null=True, upload_to="carsoul_product/{{name}}"
            ),
        ),
        migrations.AlterField(
            model_name="product_carsoule",
            name="pic3",
            field=models.FileField(
                max_length=250, null=True, upload_to="carsoul_product/{{name}}"
            ),
        ),
        migrations.AlterField(
            model_name="product_carsoule",
            name="pic4",
            field=models.FileField(
                max_length=250, null=True, upload_to="carsoul_product/{{name}}"
            ),
        ),
        migrations.AlterField(
            model_name="product_carsoule",
            name="pic5",
            field=models.FileField(
                max_length=250, null=True, upload_to="carsoul_product/{{name}}"
            ),
        ),
        migrations.AlterField(
            model_name="product_carsoule",
            name="product_added_time",
            field=models.TimeField(
                default=datetime.datetime(2024, 3, 25, 16, 16, 56, 683229)
            ),
        ),
    ]
