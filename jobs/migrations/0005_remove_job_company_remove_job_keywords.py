# Generated by Django 5.1.7 on 2025-04-01 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0004_alter_job_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="company",
        ),
        migrations.RemoveField(
            model_name="job",
            name="keywords",
        ),
    ]
