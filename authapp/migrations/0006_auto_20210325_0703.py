# Generated by Django 2.2.17 on 2021-03-25 04:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20210325_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 4, 3, 26, 22485, tzinfo=utc)),
        ),
    ]