# Generated by Django 4.1 on 2023-02-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0032_event_menu_emi_peice'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_menu',
            name='emi_category',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event_menu',
            name='event_id',
            field=models.IntegerField(),
        ),
    ]
