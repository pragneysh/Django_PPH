# Generated by Django 4.1 on 2022-12-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(db_column='Admin_ID', primary_key=True, serialize=False)),
                ('admin_name', models.CharField(db_column='Admin_Name', max_length=50)),
                ('admin_password', models.CharField(db_column='Admin_Password', max_length=8)),
                ('email_id', models.CharField(db_column='Email_ID', max_length=50)),
                ('contact_number', models.BigIntegerField(db_column='Contact_Number')),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='App1FoodCategory',
            fields=[
                ('fc_id', models.AutoField(primary_key=True, serialize=False)),
                ('fc_name', models.CharField(max_length=100, unique=True)),
                ('fc_description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'app_1_food_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='App1Fooditem',
            fields=[
                ('fi_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=100, unique=True)),
                ('categories', models.CharField(max_length=100)),
                ('food_price', models.IntegerField()),
                ('food_description', models.CharField(max_length=1000)),
                ('food_image', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'app_1_fooditem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='App1TableBooking',
            fields=[
                ('tb_name', models.CharField(max_length=100)),
                ('tb_contact', models.CharField(max_length=10)),
                ('tb_email', models.CharField(max_length=254)),
                ('tb_no_guest', models.IntegerField()),
                ('tb_date', models.DateField()),
                ('tb_time', models.TextField()),
                ('table_type', models.TextField()),
                ('tb_choose', models.CharField(max_length=10)),
                ('tb_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'app_1_table_booking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='App1Usersmodel',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('u_address', models.CharField(max_length=100)),
                ('u_city', models.CharField(max_length=100)),
                ('u_pin_code', models.IntegerField(blank=True, null=True)),
                ('user_image', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'app_1_usersmodel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'django_site',
                'managed': False,
            },
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
            options={
                'db_table': 'event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HallBooking',
            fields=[
                ('hall_booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_person', models.IntegerField(db_column='No_Person')),
                ('date_time_start_field', models.DateTimeField(db_column='Date/Time(Start)')),
                ('time_end_field', models.TimeField(db_column='Time(End)')),
                ('fun_info', models.CharField(db_column='Fun_Info', max_length=500)),
            ],
            options={
                'db_table': 'hall_booking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PartyOrder',
            fields=[
                ('party_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField(db_column='Customer_ID')),
                ('event_id', models.IntegerField()),
            ],
            options={
                'db_table': 'party_order',
                'managed': False,
            },
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
                ('food_image', models.ImageField(upload_to='pic/')),
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
            field=models.CharField(default='nothing', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersmodel',
            name='u_city',
            field=models.CharField(default='nothing', max_length=100),
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
    ]