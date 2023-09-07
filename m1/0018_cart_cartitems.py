# Generated by Django 4.1 on 2023-01-13 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0017_alter_order_details_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='app_1.usersmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('usersmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_1.usersmodel')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_tems', to='app_1.cart')),
                ('fooditem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.fooditem')),
            ],
            bases=('app_1.usersmodel',),
        ),
    ]
