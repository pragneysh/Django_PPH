# Generated by Django 4.1 on 2023-01-21 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0006_alter_fooditem_food_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.order'),
        ),
    ]
