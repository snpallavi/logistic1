# Generated by Django 4.0.3 on 2022-04-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='capacity',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='size',
            field=models.CharField(max_length=10),
        ),
    ]