# Generated by Django 3.0.6 on 2020-05-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200526_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('C', 'Completed'), ('IP', 'In progress'), ('N', 'New')], default='N', max_length=100),
        ),
    ]
