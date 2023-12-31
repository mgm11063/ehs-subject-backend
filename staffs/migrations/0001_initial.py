# Generated by Django 4.2.7 on 2023-12-01 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("opinions", "0001_initial"),
        ("segs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="G_examination",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="S_examination",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("name", models.CharField(max_length=10)),
                ("is_office", models.BooleanField(default=False)),
                ("is_night", models.BooleanField(default=False)),
                ("join_date", models.DateField()),
                ("pre_examination_date", models.DateField(null=True)),
                (
                    "g_examination",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="staffs",
                        to="staffs.g_examination",
                    ),
                ),
                (
                    "opinions",
                    models.ManyToManyField(
                        related_name="staffs", to="opinions.opinion"
                    ),
                ),
                (
                    "s_examination",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="staffs",
                        to="staffs.s_examination",
                    ),
                ),
                (
                    "segs",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="staffs",
                        to="segs.seg",
                    ),
                ),
            ],
        ),
    ]
