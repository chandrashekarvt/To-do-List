# Generated by Django 3.0.5 on 2020-07-23 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200604_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date_added',
            field=models.DateField(default=datetime.date(2020, 7, 23)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='due_date',
            field=models.DateField(default=datetime.date(2020, 7, 23)),
        ),
    ]
