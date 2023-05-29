# Generated by Django 4.2.1 on 2023-05-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RecommendCos",
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
                ("index", models.IntegerField(blank=True, null=True)),
                ("title", models.TextField(blank=True, null=True)),
                ("recom_movie", models.TextField(blank=True, null=True)),
                ("imdb_id", models.TextField(blank=True, null=True)),
            ],
            options={"db_table": "recommend_cos",},
        ),
    ]
