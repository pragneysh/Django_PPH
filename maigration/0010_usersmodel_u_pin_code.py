# Generated by Django 4.1 on 2022-12-17 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0009_usersmodel_u_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersmodel',
            name='u_pin_code',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
    ]
