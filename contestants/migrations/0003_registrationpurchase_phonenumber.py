# Generated by Django 4.0.4 on 2022-05-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0002_registrationpurchase_delete_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationpurchase',
            name='phonenumber',
            field=models.CharField(default='08000000000', max_length=15),
        ),
    ]
