# Generated by Django 3.0.6 on 2020-05-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200526_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('IN-PROGRESS', 'In progress'), ('COMPLETED', 'Completed')], default='NEW', max_length=100),
        ),
    ]
