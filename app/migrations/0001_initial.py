# Generated by Django 4.1.7 on 2023-03-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Component",
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
                ("name", models.CharField(max_length=200)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("published", "published"),
                            ("draft", "draft"),
                            ("active", "active"),
                        ],
                        default="published",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "db_table": "task-table",
            },
        ),
    ]