# Generated by Django 3.2.4 on 2021-06-09 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 6, 10, 1, 23, 41, 630383))),
                ('name', models.TextField()),
                ('e_mail', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('service', models.CharField(max_length=15)),
                ('message', models.TextField()),
            ],
        ),
    ]
