# Generated by Django 4.1 on 2023-03-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0041_alter_order_items_alter_order_t_p'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servise_area',
            fields=[
                ('sa_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('sa_name', models.CharField(max_length=500)),
                ('pin_code', models.IntegerField()),
            ],
        ),
    ]
