# Generated by Django 4.2.6 on 2023-10-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_address_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='raw_password',
            field=models.CharField(db_column='fld_raw_password', default='', max_length=25),
        ),
    ]
