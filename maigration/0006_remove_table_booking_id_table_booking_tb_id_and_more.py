# Generated by Django 4.1 on 2022-12-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_table_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_booking',
            name='id',
        ),
        migrations.AddField(
            model_name='table_booking',
            name='tb_id',
            field=models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='table_booking',
            name='tb_time',
            field=models.TextField(),
        ),
    ]
