# Generated by Django 4.0.2 on 2023-10-28 14:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0002_cinemahall_movie_moviesession"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cinemahall",
            old_name="row",
            new_name="rows",
        ),
    ]
