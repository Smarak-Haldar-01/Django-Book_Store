# Generated by Django 5.0.3 on 2024-03-31 08:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0028_reportproblem_2_problem_pic"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reportproblem_1",
            old_name="problrm_time",
            new_name="problem_time",
        ),
        migrations.RenameField(
            model_name="reportproblem_1",
            old_name="order_date",
            new_name="report_date",
        ),
        migrations.RenameField(
            model_name="reportproblem_2",
            old_name="problrm_time",
            new_name="problem_time",
        ),
        migrations.RenameField(
            model_name="reportproblem_2",
            old_name="order_date",
            new_name="report_date",
        ),
    ]