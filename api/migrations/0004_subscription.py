# Generated by Django 4.0.3 on 2022-04-07 22:11

from django.db import migrations, models
import xmlrpc.client


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_vehicle_capacity_alter_vehicle_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_plan_name', models.CharField(max_length=200)),
                ('price', models.FloatField(max_length=10)),
                ('validity_period', models.DateTimeField(verbose_name=xmlrpc.client.DateTime)),
            ],
        ),
    ]