# Generated by Django 3.1 on 2020-09-18 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200918_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='tracker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.tracker', verbose_name='tracker'),
        ),
    ]
