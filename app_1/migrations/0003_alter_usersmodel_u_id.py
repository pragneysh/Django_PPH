# Generated by Django 4.1 on 2023-01-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_admin_cart_event_food_category_fooditem_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='u_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
