# Generated by Django 4.1 on 2023-02-08 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0026_event_menu_category_event_menu_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_menu_category',
            name='emc_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
