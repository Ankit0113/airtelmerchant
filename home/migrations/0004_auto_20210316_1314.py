# Generated by Django 3.1.7 on 2021-03-16 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210316_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='date_note_for_use',
            field=models.DateField(default=datetime.datetime(2021, 3, 16, 13, 14, 46, 601680)),
        ),
    ]
