# Generated by Django 5.1.7 on 2025-03-30 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0004_alter_job_company"),
        ("user", "0003_delete_company_alter_user_managers_company"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Company",
        ),
        migrations.CreateModel(
            name="Company",
            fields=[],
            options={
                "verbose_name": "Company",
                "verbose_name_plural": "Companies",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("user.user",),
        ),
    ]
