# Generated by Django 4.0.3 on 2022-07-18 15:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AwardsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='AwardsContestant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('instagram_handle', models.CharField(max_length=30)),
                ('tell_us', models.TextField(default='I WANT TO WIN')),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=20)),
                ('image1', models.ImageField(default='defaultuser.jpg', upload_to='contestant/%Y/%m/%d')),
                ('image2', models.ImageField(default='defaultuser.jpg', upload_to='contestant/%Y/%m/%d')),
                ('gender', models.CharField(max_length=10)),
                ('number_of_votes', models.IntegerField(default=0)),
                ('is_evicted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('category', models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.SET_DEFAULT, to='award.awardscategory')),
            ],
        ),
    ]