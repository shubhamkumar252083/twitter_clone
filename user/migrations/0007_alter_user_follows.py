# Generated by Django 4.2.6 on 2023-11-21 13:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(db_column='fld_followers', db_table='tbl_user_follows', related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
