# Generated by Django 4.2.6 on 2023-10-30 08:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(db_column='fld_followers', related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
