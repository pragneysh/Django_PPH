# Generated by Django 4.1 on 2023-01-07 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0014_order_order_status_order_total_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('order_d_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('fi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.fooditem')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.order')),
            ],
        ),
    ]
