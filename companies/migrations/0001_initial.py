# Generated by Django 4.2.7 on 2023-11-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("staffs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(default="", max_length=150)),
                (
                    "staffs",
                    models.ManyToManyField(related_name="companys", to="staffs.staff"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
