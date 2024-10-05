# Generated by Django 4.2.16 on 2024-10-05 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                ("id_city", models.AutoField(primary_key=True, serialize=False)),
                (
                    "city_name_en",
                    models.CharField(
                        max_length=255, verbose_name="City Name (English)"
                    ),
                ),
                (
                    "city_name_ru",
                    models.CharField(
                        max_length=255, verbose_name="City Name (Russian)"
                    ),
                ),
                (
                    "city_name_kk",
                    models.CharField(max_length=255, verbose_name="City Name (Kazakh)"),
                ),
                ("population", models.IntegerField(verbose_name="Population")),
                (
                    "area",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Area in sq.km"
                    ),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        decimal_places=7, max_digits=10, verbose_name="Latitude"
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        decimal_places=7, max_digits=10, verbose_name="Longitude"
                    ),
                ),
            ],
            options={
                "verbose_name": "City",
                "verbose_name_plural": "Cities",
            },
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                ("id_region", models.AutoField(primary_key=True, serialize=False)),
                (
                    "region_name_en",
                    models.CharField(
                        max_length=255, verbose_name="Region Name (English)"
                    ),
                ),
                (
                    "region_name_ru",
                    models.CharField(
                        max_length=255, verbose_name="Region Name (Russian)"
                    ),
                ),
                (
                    "region_name_kk",
                    models.CharField(
                        max_length=255, verbose_name="Region Name (Kazakh)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Region",
                "verbose_name_plural": "Regions",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=1,
                        verbose_name="Gender",
                    ),
                ),
                ("age", models.PositiveIntegerField(verbose_name="Age")),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="predictions.city",
                        verbose_name="City",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "User Profile",
                "verbose_name_plural": "User Profiles",
            },
        ),
        migrations.CreateModel(
            name="District",
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
                    "district_name_en",
                    models.CharField(
                        max_length=255, verbose_name="District Name (English)"
                    ),
                ),
                (
                    "district_name_ru",
                    models.CharField(
                        max_length=255, verbose_name="District Name (Russian)"
                    ),
                ),
                (
                    "district_name_kk",
                    models.CharField(
                        max_length=255, verbose_name="District Name (Kazakh)"
                    ),
                ),
                ("population", models.IntegerField(verbose_name="Population")),
                (
                    "area",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Area in sq.km"
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="districts",
                        to="predictions.city",
                        verbose_name="City",
                    ),
                ),
            ],
            options={
                "verbose_name": "District",
                "verbose_name_plural": "Districts",
            },
        ),
        migrations.AddField(
            model_name="city",
            name="region",
            field=models.ForeignKey(
                db_column="id_region",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cities",
                to="predictions.region",
                verbose_name="Region",
            ),
        ),
    ]
