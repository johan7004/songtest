# Generated by Django 3.1.6 on 2021-03-06 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_songs_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songs',
            old_name='name',
            new_name='title',
        ),
    ]
