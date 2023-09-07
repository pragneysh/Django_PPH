from django.db import models

# Create your models here.


class UsersModel(models.Model):
    u_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    # re_password = models.CharField(max_length=100)
    u_address = models.CharField(max_length=100)
    u_city = models.CharField(max_length=100)
    u_pin_code = models.IntegerField(null=True)
    user_image = models.ImageField(upload_to='pic/', default="")


class Food_category(models.Model):
    fc_id = models.IntegerField(primary_key=True)
    fc_name = models.CharField(max_length=100, unique=True)
    fc_description = models.CharField(max_length=1000)


class FoodItem(models.Model):
    fi_id = models.IntegerField(primary_key=True, auto_created=True)
    food_name = models.CharField(max_length=100, unique=True)
    categories = models.CharField(max_length=100)
    food_price = models.IntegerField()
    food_description = models.CharField(max_length=1000)
    food_image = models.ImageField(upload_to='pic/')


class Table_Booking(models.Model):
    tb_id = models.IntegerField(primary_key=True, auto_created=True)
    tb_name = models.CharField(max_length=100)
    tb_contact = models.CharField(max_length=10)
    tb_email = models.EmailField()
    tb_no_guest = models.IntegerField()
    tb_date = models.DateField()
    tb_time = models.TextField()
    table_type = models.TextField(max_length=25)
    tb_choose = models.CharField(max_length=10)


class App1Usersmodel(models.Model):
    u_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=100)
    u_address = models.CharField(max_length=100)
    u_city = models.CharField(max_length=100)
    u_pin_code = models.IntegerField(blank=True, null=True)
    user_image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app_1_usersmodel'


class App1TableBooking(models.Model):
    tb_name = models.CharField(max_length=100)
    tb_contact = models.CharField(max_length=10)
    tb_email = models.CharField(max_length=254)
    tb_no_guest = models.IntegerField()
    tb_date = models.DateField()
    tb_time = models.TextField()
    table_type = models.TextField()
    tb_choose = models.CharField(max_length=10)
    tb_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'app_1_table_booking'


class App1Fooditem(models.Model):
    fi_id = models.AutoField(primary_key=True)
    food_name = models.CharField(unique=True, max_length=100)
    categories = models.CharField(max_length=100)
    food_price = models.IntegerField()
    food_description = models.CharField(max_length=1000)
    food_image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app_1_fooditem'

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_what = models.CharField(max_length=500)
    event_date_time = models.DateField()
    delivery_add = models.CharField(max_length=100)
    number_of_person = models.IntegerField()
    # Field name made lowercase.
    alt_contactno = models.BigIntegerField(db_column='alt_contactNO')

    class Meta:
        managed = False
        db_table = 'event'


#  django



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'
