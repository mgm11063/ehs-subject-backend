# Generated by Django 4.2.4 on 2023-10-10 02:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Factor",
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
                ("value", models.CharField(max_length=100)),
                ("label", models.CharField(editable=False, max_length=100)),
                (
                    "check_cycle",
                    models.IntegerField(
                        blank=True,
                        default=6,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(12),
                        ],
                    ),
                ),
                (
                    "regular_check_cycle",
                    models.IntegerField(
                        blank=True,
                        default=12,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(6),
                            django.core.validators.MaxValueValidator(24),
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Seg",
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
                ("name", models.CharField(max_length=80)),
                (
                    "factors",
                    models.ManyToManyField(
                        blank=True, null=True, related_name="segs", to="segs.factor"
                    ),
                ),
            ],
        ),
    ]
