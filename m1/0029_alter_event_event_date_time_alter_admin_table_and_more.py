# Generated by Django 4.1 on 2023-01-19 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0028_delete_app1foodcategory_delete_app1fooditem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date_time',
            field=models.DateField(),
        ),
        migrations.AlterModelTable(
            name='admin',
            table=None,
        ),
        migrations.AlterModelTable(
            name='event',
            table=None,
        ),
    ]
