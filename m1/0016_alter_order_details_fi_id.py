# Generated by Django 4.1 on 2023-01-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0015_order_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='fi_id',
            field=models.IntegerField(),
        ),
    ]
