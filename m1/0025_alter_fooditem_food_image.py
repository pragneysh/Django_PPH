# Generated by Django 4.1 on 2023-01-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0024_alter_fooditem_food_image_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='food_image',
            field=models.ImageField(default='', upload_to='pic/'),
        ),
    ]
