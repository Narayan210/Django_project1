# Generated by Django 4.2.5 on 2023-09-29 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='titel',
            new_name='title',
        ),
    ]