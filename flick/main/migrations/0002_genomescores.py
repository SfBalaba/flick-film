# Generated by Django 4.2.1 on 2023-06-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GenomeScores",
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
                (
                    "movieid",
                    models.IntegerField(blank=True, db_column="movieId", null=True),
                ),
                (
                    "tagid",
                    models.IntegerField(blank=True, db_column="tagId", null=True),
                ),
                ("relevance", models.FloatField(blank=True, null=True)),
            ],
            options={"db_table": "genome_scores", "managed": False,},
        ),
    ]
