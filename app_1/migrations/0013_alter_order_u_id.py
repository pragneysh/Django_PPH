# Generated by Django 4.1 on 2023-01-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0012_alter_order_u_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_id',
            field=models.IntegerField(),
        ),
    ]
