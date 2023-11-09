# Generated by Django 4.2.7 on 2023-11-07 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coords",
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
                ("latitude", models.FloatField(blank=True, max_length=5)),
                ("longitude", models.FloatField(blank=True, max_length=5)),
                ("height", models.IntegerField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name="PerevalImage",
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
                ("image", models.ImageField(blank=True, null=True, upload_to="media/")),
            ],
        ),
        migrations.CreateModel(
            name="Season",
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
                (
                    "winter",
                    models.CharField(
                        choices=[
                            ("", "не указано"),
                            ("1A", "1a"),
                            ("1B", "1б"),
                            ("2А", "2а"),
                            ("2В", "2б"),
                            ("3А", "3а"),
                            ("3В", "3б"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "spring",
                    models.CharField(
                        choices=[
                            ("", "не указано"),
                            ("1A", "1a"),
                            ("1B", "1б"),
                            ("2А", "2а"),
                            ("2В", "2б"),
                            ("3А", "3а"),
                            ("3В", "3б"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "summer",
                    models.CharField(
                        choices=[
                            ("", "не указано"),
                            ("1A", "1a"),
                            ("1B", "1б"),
                            ("2А", "2а"),
                            ("2В", "2б"),
                            ("3А", "3а"),
                            ("3В", "3б"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "autumn",
                    models.CharField(
                        choices=[
                            ("", "не указано"),
                            ("1A", "1a"),
                            ("1B", "1б"),
                            ("2А", "2а"),
                            ("2В", "2б"),
                            ("3А", "3а"),
                            ("3В", "3б"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Users",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(max_length=12)),
                ("fam", models.CharField(max_length=30)),
                ("name", models.CharField(max_length=30)),
                ("otc", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PerevalAdded",
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
                (
                    "beautyTitle",
                    models.CharField(
                        choices=[
                            ("poss", "перевал"),
                            ("gorge", "ущелье"),
                            ("plateau", "плато"),
                        ],
                        max_length=20,
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("other_titles", models.CharField(max_length=30)),
                ("connect", models.TextField()),
                ("add_time", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "новый"),
                            ("pending", "на модерации"),
                            ("accepted", "принят"),
                            ("rejected", "не принят"),
                        ],
                        default="new",
                        max_length=20,
                    ),
                ),
                (
                    "coords",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pereval_app.coords",
                    ),
                ),
                (
                    "images",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pereval_app.perevalimage",
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pereval_app.season",
                    ),
                ),
                (
                    "users",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pereval_app.users",
                    ),
                ),
            ],
        ),
    ]
