# Generated by Django 4.1 on 2022-12-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0004_alter_admin_admin_id_alter_admin_admin_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_category',
            name='fc_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usersmodel',
            name='u_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]