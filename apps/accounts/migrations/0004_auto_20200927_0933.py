# Generated by Django 3.1 on 2020-09-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userverification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userverification',
            old_name='bank_account_number',
            new_name='account_number',
        ),
        migrations.AddField(
            model_name='userverification',
            name='account_name',
            field=models.CharField(default='Bank Name', max_length=50, verbose_name='bank account name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userverification',
            name='id_type',
            field=models.CharField(default='Voters card', max_length=20, verbose_name='type of ID'),
            preserve_default=False,
        ),
    ]
