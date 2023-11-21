# Generated by Django 4.2.6 on 2023-10-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.BigAutoField(db_column='fld_ai_id', primary_key=True, serialize=False)),
                ('email', models.EmailField(db_column='fld_email', max_length=100, unique=True, verbose_name='Email')),
                ('mobile', models.CharField(db_column='fld_mobile', max_length=100, unique=True)),
                ('password', models.CharField(db_column='fld_password', max_length=255)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, db_column='fld_created_datetime', null=True)),
                ('is_admin', models.BooleanField(db_column='fld_is_admin', default=False)),
            ],
            options={
                'verbose_name': 'users',
                'db_table': 'tbl_user',
            },
        ),
    ]
