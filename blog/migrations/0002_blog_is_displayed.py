# Generated by Django 4.0.4 on 2022-06-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_displayed',
            field=models.BooleanField(default=True),
        ),
    ]
