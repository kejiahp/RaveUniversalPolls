# Generated by Django 4.0.4 on 2022-05-19 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0014_registercontestant_is_evicted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registercontestant',
            options={'ordering': ('-number_of_votes',)},
        ),
    ]
