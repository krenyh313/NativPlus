# Generated by Django 3.0.6 on 2020-07-19 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CurrentLocation', models.CharField(max_length=60)),
                ('Destination', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('passengers', models.IntegerField()),
                ('smoking', models.BooleanField()),
                ('pets', models.BooleanField()),
                ('music', models.BooleanField()),
                ('rating', models.FloatField(default=0)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
