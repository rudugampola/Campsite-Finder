# Generated by Django 5.1.4 on 2025-01-01 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Facility",
            fields=[
                (
                    "facility_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "parent_org_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "type_description",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("reservable", models.BooleanField(default=False)),
                ("enabled", models.BooleanField(default=True)),
                ("last_updated_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="RecreationArea",
            fields=[
                (
                    "rec_area_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "org_rec_area_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "parent_org_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("phone", models.CharField(blank=True, max_length=50, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("reservation_url", models.URLField(blank=True, null=True)),
                ("map_url", models.URLField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("enabled", models.BooleanField(default=True)),
                ("last_updated_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="RecAreaFacilityLink",
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
                    "facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="camp.facility"
                    ),
                ),
                (
                    "rec_area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="camp.recreationarea",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="facility",
            name="parent_rec_area",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="facilities",
                to="camp.recreationarea",
            ),
        ),
    ]
