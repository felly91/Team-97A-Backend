# Generated by Django 3.1 on 2020-09-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200927_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userverification',
            name='BVN',
            field=models.CharField(max_length=11, verbose_name='Bank Verification Number'),
        ),
    ]