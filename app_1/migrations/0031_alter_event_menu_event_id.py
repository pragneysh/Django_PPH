# Generated by Django 4.1 on 2023-02-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0030_event_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_menu',
            name='event_id',
            field=models.IntegerField(default='1'),
        ),
    ]
