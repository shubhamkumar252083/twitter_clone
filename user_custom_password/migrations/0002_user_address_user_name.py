# Generated by Django 4.2.6 on 2023-10-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(db_column='fld_address', default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(db_column='name', default='', max_length=100),
        ),
    ]
