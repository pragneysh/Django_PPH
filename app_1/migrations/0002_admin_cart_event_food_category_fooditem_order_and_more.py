# Generated by Django 4.1 on 2023-01-19 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_password', models.CharField(max_length=8)),
                ('email_id', models.CharField(max_length=50)),
                ('contact_number', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_what', models.CharField(max_length=500)),
                ('event_date_time', models.DateField()),
                ('delivery_add', models.CharField(max_length=100)),
                ('number_of_person', models.IntegerField()),
                ('alt_contactno', models.BigIntegerField(db_column='alt_contactNO')),
            ],
        ),
        migrations.CreateModel(
            name='Food_category',
            fields=[
                ('fc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fc_name', models.CharField(max_length=100, unique=True)),
                ('fc_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('fi_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=100, unique=True)),
                ('categories', models.CharField(max_length=100)),
                ('food_price', models.IntegerField()),
                ('food_description', models.CharField(max_length=1000)),
                ('food_image', models.ImageField(default='', upload_to='pic1/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('u_id', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('order_date', models.DateField()),
                ('order_time', models.TimeField()),
                ('order_status', models.CharField(default='Confirm', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('order_d_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=100)),
                ('fi_id', models.IntegerField()),
                ('fi_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Table_Booking',
            fields=[
                ('tb_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('tb_name', models.CharField(max_length=100)),
                ('tb_contact', models.CharField(max_length=10)),
                ('tb_email', models.EmailField(max_length=254)),
                ('tb_no_guest', models.IntegerField()),
                ('tb_date', models.DateField()),
                ('tb_time', models.TextField()),
                ('table_type', models.TextField(max_length=25)),
                ('tb_choose', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='usersmodel',
            name='u_address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersmodel',
            name='u_city',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersmodel',
            name='u_pin_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usersmodel',
            name='user_image',
            field=models.ImageField(default='', upload_to='pic/'),
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
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='app_1.usersmodel'),
        ),
    ]
