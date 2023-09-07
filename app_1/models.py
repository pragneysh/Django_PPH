
from django.db import models


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50)
    admin_password = models.CharField(max_length=8)
    email_id = models.CharField(max_length=50)
    contact_number = models.BigIntegerField()


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
    food_image = models.ImageField(upload_to='FOOD_IMAGE/', default="")


class UsersModel(models.Model):
    u_id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    u_address = models.CharField(max_length=100)
    u_city = models.CharField(max_length=100)
    u_pin_code = models.IntegerField(null=True)
    user_image = models.ImageField(upload_to='User_Image/', default="")


class Table_Booking(models.Model):
    tb_id = models.IntegerField(primary_key=True, auto_created=True)
    u_id = models.IntegerField()
    tb_name = models.CharField(max_length=100)
    tb_contact = models.CharField(max_length=10)
    tb_email = models.EmailField()
    tb_no_guest = models.IntegerField()
    tb_date = models.DateField()
    tb_time = models.TextField()
    table_type = models.IntegerField()
    tb_choose = models.CharField(max_length=10)


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True, auto_created=True)
    u_id = models.IntegerField()
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    order_date = models.DateField()
    order_time = models.TimeField()
    order_status = models.CharField(max_length=10, default="Pending")
    t_p = models.IntegerField(null=True)
    items = models.IntegerField(null=True)


class Order_Details(models.Model):
    order_d_id = models.IntegerField(primary_key=True, auto_created=True)
    order_id = models.IntegerField()
    fi_id = models.IntegerField()
    fi_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    t_price = models.IntegerField()



class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_what = models.CharField(max_length=500)
    event_date_time = models.DateField()
    delivery_add = models.CharField(max_length=100)
    number_of_person = models.IntegerField()
    u_id = models.IntegerField()
    alt_contactno = models.BigIntegerField(db_column='alt_contactNO')
    p_price = models.IntegerField(null=True)
    a_price = models.IntegerField(null=True)


class Hall_Booking(models.Model):
    hb_id = models.AutoField(primary_key=True)  
    date = models.DateField()
    start_time = models.TextField() 
    end_time = models.TextField()
    event_id = models.IntegerField()
    u_id = models.IntegerField()


class Event_menu_category(models.Model):
    emc_id = models.IntegerField(primary_key=True, auto_created=True)
    emc_name = models.CharField(max_length=100, unique=True)
    emc_description = models.CharField(max_length=1000)

class Event_menu_item(models.Model):
    emi_id = models.AutoField(primary_key=True, auto_created=True)
    emi_name = models.CharField(max_length=500)
    emi_price = models.IntegerField()
    emi_category = models.CharField(max_length=100)
    emi_lavel = models.IntegerField()

class Event_menu(models.Model):
    em_id = models.AutoField(primary_key=True, auto_created=True)
    event_id = models.IntegerField()
    u_id = models.IntegerField()
    emi_id = models.IntegerField()
    emi_peice = models.IntegerField()
    emi_category = models.CharField(max_length=500)
    emi_name = models.CharField(max_length=500)

class Servise_area(models.Model):
    sa_id = models.AutoField(primary_key=True, auto_created=True)
    sa_name =models.CharField(max_length=500)
    pin_code = models.IntegerField()