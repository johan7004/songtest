# Generated by Django 3.1.6 on 2021-02-20 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_songs_fullsong'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='fullsong',
        ),
    ]
