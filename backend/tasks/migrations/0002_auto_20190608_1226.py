# Generated by Django 2.2.2 on 2019-06-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='completed_on',
            field=models.DateTimeField(default=None, editable=False, null=True),
        ),
    ]
