# Generated by Django 3.1 on 2020-10-06 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20201005_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='current_balance',
            field=models.FloatField(default=0),
        ),
    ]
