# Generated by Django 4.1 on 2023-01-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0010_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table_booking',
            name='table_type',
            field=models.IntegerField(),
        ),
    ]