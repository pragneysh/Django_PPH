# Generated by Django 4.1 on 2022-12-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0012_alter_usersmodel_u_pin_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersmodel',
            name='user_image',
            field=models.ImageField(default='', upload_to='pic/'),
            preserve_default=False,
        ),
    ]