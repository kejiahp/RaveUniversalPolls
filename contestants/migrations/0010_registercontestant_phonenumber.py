# Generated by Django 4.0.4 on 2022-05-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0009_alter_registercontestant_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registercontestant',
            name='phonenumber',
            field=models.CharField(default=131, max_length=20),
            preserve_default=False,
        ),
    ]
