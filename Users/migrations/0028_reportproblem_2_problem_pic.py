# Generated by Django 5.0.3 on 2024-03-31 08:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0027_reportproblem_1_problem_pic"),
    ]

    operations = [
        migrations.AddField(
            model_name="reportproblem_2",
            name="problem_pic",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]