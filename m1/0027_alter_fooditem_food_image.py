# Generated by Django 4.1 on 2023-01-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0026_alter_fooditem_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='food_image',
            field=models.ImageField(default='', upload_to='pic1/'),
        ),
    ]