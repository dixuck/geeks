# Generated by Django 4.2.7 on 2023-12-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_alter_task_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]