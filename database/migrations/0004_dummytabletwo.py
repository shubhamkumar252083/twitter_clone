# Generated by Django 4.2.6 on 2023-11-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_dummytable_mappinghashtags_dummytable_hashtag'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyTableTwo',
            fields=[
                ('id', models.AutoField(db_column='fld_ai_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='fld_name', max_length=100, unique=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, db_column='fld_created_datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='fld_updated_at')),
                ('hashtag', models.ManyToManyField(db_column='fld_hashtags2', db_table='custom_hashtag_n_dummy_relation', related_name='hashtags_relation2', to='database.hashtag')),
            ],
            options={
                'db_table': 'tbl_dummy_two',
            },
        ),
    ]
