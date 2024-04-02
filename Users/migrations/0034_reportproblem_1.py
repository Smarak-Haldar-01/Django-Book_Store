# Generated by Django 5.0.3 on 2024-03-31 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0033_delete_reportproblem_1"),
    ]

    operations = [
        migrations.CreateModel(
            name="reportProblem_1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("umail", models.EmailField(max_length=254)),
                ("utype", models.CharField(max_length=20)),
                ("report_title", models.TextField()),
                ("explain", models.TextField()),
                ("problem_pic", models.FileField(null=True, upload_to="")),
                ("problem_date", models.DateField()),
                ("problem_time", models.TimeField()),
                ("report_date", models.DateTimeField(auto_now_add=True)),
                (
                    "uid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Users.user"
                    ),
                ),
            ],
        ),
    ]