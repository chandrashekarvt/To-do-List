# Generated by Django 3.0.6 on 2020-05-26 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200526_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date_added',
            field=models.DateField(default=datetime.date(2020, 5, 26)),
        ),
    ]
