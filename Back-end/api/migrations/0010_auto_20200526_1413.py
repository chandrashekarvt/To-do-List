# Generated by Django 3.0.6 on 2020-05-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_tasks_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='label',
            field=models.CharField(choices=[('PERSONAL', 'Personal'), ('WORK', 'Work'), ('SHOPPING', 'Shopping'), ('OTHERS', 'Others')], default='PERSONAL', max_length=100),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'Completed'), ('IN-PROGRESS', 'In progress'), ('NEW', 'New')], default='N', max_length=100),
        ),
    ]