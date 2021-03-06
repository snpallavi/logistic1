# Generated by Django 4.0.3 on 2022-04-07 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleTypeName', models.CharField(max_length=100)),
                ('capacity', models.FloatField(max_length=10)),
                ('size', models.FloatField(max_length=10)),
                ('details', models.CharField(max_length=100)),
                ('price_per_km', models.FloatField(max_length=10)),
            ],
        ),
    ]
