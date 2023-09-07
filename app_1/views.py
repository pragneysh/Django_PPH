from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session
from django.contrib import messages
from datetime import date
from datetime import datetime
from django.utils import timezone
from django.shortcuts import HttpResponseRedirect
# from tkinter import messagebox
from app_1.models import *
# from app_1.models import Hall
from operator import itemgetter
import mysql.connector as sql
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# BASE
# request.session['cart'] = None


def admin_login(request):
    return render(request, "admin.html")


def login_admin(request):
    if request.method == "POST":
        name = request.POST['admin_name']
        password = request.POST['pswrd']
        admin = Admin.objects.all()
        for i in admin:
            if name == i.admin_name:
                data = Admin.objects.get(admin_name=name)
                if data.admin_password == password:
                    request.session['admin_name'] = i.admin_name
                    # request.session['u_id'] = data.admin_id
                    request.session['admin_id'] = data.admin_id
                    request.session['name'] = None
                    request.session['contact'] = None
                    request.session['u_id'] = None
                    return redirect('dashboard')
        else:
            messages.success(request, 'User name and Passwrod does not match')
            return redirect('admin_login')


def admin_logout(request):
    request.session['admin_name'] = None
    request.session['u_id'] = None
    request.session['admin_id'] = None
    return redirect('admin_login')


def base(request):
    cart = request.session['cart']
    c = 0
    for i in cart:
        c = c+1
    return render(request, "base.html")


def admin_base(request):
    return render(request, "admin_base.html")


def display(request):
    return render(request, "display.html")


def update(request):
    return render(request, "update.html")


def add(request):
    return render(request, "add.html")


def home(request):
    admin = request.session.get('admin_id')
    try:
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "index.html", {'admin': admin, 'u_id': u_id, 'user': user})
    except:
        return render(request, "index.html", {'admin': admin})


def dishes(request):
    if request.session.get('u_id'):
        return render(request, "dishes.html")
    else:
        return redirect('login_page')


def table(request):
    fc = Food_category.objects.all()
    admin = request.session.get('admin_id')
    fi = FoodItem.objects.all()
    try:
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "table.html", {'fc': fc, 'fi': fi, 'admin': admin, 'u_id': u_id, 'user': user})
    except:
        return render(request, "table.html", {'fc': fc, 'fi': fi, 'admin': admin})


def menu(request):
    fc = Food_category.objects.all()
    fi = FoodItem.objects.all()
    admin = request.session.get('admin_id')
    cart = request.session.get('cart')
    try:
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        if cart != None:
            c = 0
            for i in cart:
                c = c+1
            return render(request, "menu.html", {'fc': fc, 'fi': fi, 'admin': admin, 'u_id': u_id, 'user': user, 'c': c})
        return render(request, "menu.html", {'fc': fc, 'fi': fi, 'admin': admin, 'u_id': u_id, 'user': user})
    except:
        return render(request, "menu.html", {'fc': fc, 'fi': fi, 'admin': admin})


def about(request):
    admin = request.session.get('admin_id')
    try:
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "about.html", {'admin': admin, 'u_id': u_id, 'user': user})
    except:
        return render(request, "about.html", {'admin': admin})


# LOGIN


def login_page(request):
    return render(request, "login.html")


def registeruser(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        c_len = len(contact)
        user_obj = UsersModel.objects.filter(contact=contact)
        if password != re_password:
            messages.success(request, 'Both password is not same')
            return redirect('login_page')
        elif user_obj.exists():
            messages.error(request, "User alredy Exist")
            return redirect('login_page')
        elif c_len != 10:
            messages.success(request, 'Please enter correct mobile number')
            return redirect('login_page')
        else:
            user = UsersModel(
                name=name,
                contact=contact,
                email=email,
                password=password)
            user.save()
            messages.success(request, 'Ragisteration successfull')
            return redirect('user_account')
    return render(request, 'login.html')


def loginuser(request):
    if request.method == "POST":
        l_no = request.POST['l_no']
        l_password = request.POST['l_password']
        data = UsersModel.objects.filter(contact=l_no).first()
        if data is None:
            messages.error(request, "User doesn't exist")
            return render(request, 'login.html')
        else:
            if data.password == l_password:
                request.session['name'] = data.name
                request.session['contact'] = data.contact
                request.session['u_id'] = data.u_id
                request.session['admin_name'] = None
                request.session['admin_id'] = None
                return redirect('home')
            else:
                messages.error(request, "login Unsuccessfull")
                return render(request, 'login.html')


def logout(request):
    request.session.clear()
    request.session['name'] = None
    request.session['contact'] = None
    return redirect('login_page')


# CUSTOMER


def customer_detail(request):
    user = UsersModel.objects.all()
    return render(request, "customer_detail.html", {'user': user})


def user_account(request):
    if request.session.get('u_id'):
        u_id = request.session['u_id']
        name = request.session['name']
        contact = request.session['contact']
        user_data = UsersModel.objects.filter(contact=contact)
        order = Order.objects.all()
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "acount.html", {'user': user, 'order': order, 'name': name, 'u_id': u_id, "user_data": user_data})
    else:
        return redirect('login_page')


def delete_data(request, id):
    if request.session.get('admin_id'):
        user = UsersModel.objects.get(u_id=id)
        user.delete()
        return redirect('customer_detail')
    else:
        return redirect('admin_login')


def edit_form(request, id):
    if request.session.get('u_id'):
        user = UsersModel.objects.get(u_id=id)
        return render(request, "updet_user.html", {'data': user})
    else:
        return redirect('login_page')


def update_user(request, id):
    user = UsersModel.objects.get(u_id=id)
    user.name = request.POST['name']
    user.contact = request.POST['contact']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.u_address = request.POST['u_address']
    user.u_city = request.POST['u_city']
    user.u_pin_code = request.POST['u_pin_code']
    user.save()
    return redirect('user_account')


def edit_image(request, id):
    if request.session.get('u_id'):
        user = UsersModel.objects.get(u_id=id)
        return render(request, "updet_image.html", {'data': user})
    else:
        return redirect('login_page')


def update_image(request, id):
    user = UsersModel.objects.get(u_id=id)
    user.user_image = request.FILES['user_image']
    user.save()
    return redirect('edit_form', id=id)


# FOOD ITEM


def food_Item_detail(request):
    if request.session.get('admin_id'):
        fi = FoodItem.objects.all()
        return render(request, "food_Item_detail.html", {'fi': fi})
    else:
        return redirect('admin_login')


def food_Item_detail_pdf(request):
    if request.session.get('admin_id'):
        fi = FoodItem.objects.all()
        template_path = 'food_Item_detail_pdf.html'
        context = {'fi': fi}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="food_Item_detail_pdf.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    else:
        return redirect('admin_login')


def createitem(request):
    if request.session.get('admin_id'):
        fc = Food_category.objects.all()
        if request.method == "POST":
            food_name = request.POST['food_name']
            categories = request.POST['categories']
            food_price = request.POST['food_price']
            food_description = request.POST['food_description']
            food_image = request.FILES['food_image']
            fi = FoodItem(
                food_name=food_name,
                categories=categories,
                food_price=food_price,
                food_description=food_description,
                food_image=food_image)
            fi.save()
            return redirect('food_Item_detail')
        return render(request, 'createItem.html', {'fc': fc})
    else:
        return redirect('admin_login')


def edit_fi(request, fi_id):
    if request.session.get('admin_id'):
        fi = FoodItem.objects.get(fi_id=fi_id)
        fc = Food_category.objects.all()
        return render(request, "updet_food_item.html", {'data_fi': fi, 'fc': fc})
    else:
        return redirect('admin_login')


def update_fi(request, fi_id):
    if request.session.get('admin_id'):
        fi = FoodItem.objects.all()
        fi = FoodItem.objects.get(fi_id=fi_id)
        fi.food_name = request.POST['food_name']
        fi.categories = request.POST['categories']
        fi.food_price = request.POST['food_price']
        fi.food_description = request.POST['food_description']
        fi.save()
        return redirect('food_Item_detail')
    else:
        return redirect('admin_login')


def edit_food_image(request, id):
    if request.session.get('admin_id'):
        fi = FoodItem.objects.get(fi_id=id)
        return render(request, "updet_food_image.html", {'data_fi': fi})
    else:
        return redirect('admin_login')


def update_food_image(request, id):
    if request.session.get('admin_id'):
        fi = FoodItem.objects.get(fi_id=id)
        fi.food_image = request.FILES['food_image']
        fi.save()
        return redirect('edit_fi', fi_id=id)
    else:
        return redirect('admin_login')


def delete_fi(request, fi_id):
    if request.session.get('admin_id'):
        fi = FoodItem.objects.get(fi_id=fi_id)
        fi.delete()
        return redirect('food_Item_detail')
    else:
        return redirect('admin_login')


# FOOD CATOGARY


def food_category(request):
    if request.session.get('admin_id'):
        fc = Food_category.objects.all()
        return render(request, "food_category.html", {'fc': fc})
    else:
        return redirect('admin_login')


def add_food_category(request):
    if request.session.get('admin_id'):
        if request.method == "POST":
            fc_name = request.POST['fc_name']
            fc_description = request.POST['fc_description']
            fc = Food_category(
                fc_name=fc_name,
                fc_description=fc_description)
            fc.save()
            return redirect('food_category')
        return render(request, 'add_food_category.html')
    else:
        return redirect('admin_login')


def edit_fc(request, fc_id):
    if request.session.get('admin_id'):
        fc = Food_category.objects.get(fc_id=fc_id)
        return render(request, "updet_food_category.html", {'data_fc': fc})
    else:
        return redirect('admin_login')


def update_fc(request, fc_id):
    if request.session.get('admin_id'):
        fc = Food_category.objects.get(fc_id=fc_id)
        fc.fc_name = request.POST['fc_name']
        fc.fc_description = request.POST['fc_description']
        fc.save()
        return redirect('food_category')
    else:
        return redirect('admin_login')


def delete_fc(request, fc_id):
    if request.session.get('admin_id'):
        fc = Food_category.objects.get(fc_id=fc_id)
        fc.delete()
        return redirect('food_category')
    else:
        return redirect('admin_login')


def similar_fi(request, fc_id):
    # print(fc_id)
    fc = Food_category.objects.get(fc_id=fc_id)
    cat = fc.fc_name
    fi = FoodItem.objects.filter(categories=cat)
    return render(request, "similar_fi.html", {'fi': fi})


def table_booking(request):
    if request.session.get('u_id'):
        admin = request.session.get('admin_id')
        today = timezone.now().date()
        if request.method == "POST":
            tb_name = request.POST['tb_name']
            tb_contact = request.POST['tb_contact']
            tb_email = request.POST['tb_email']
            tb_no_guest_s = request.POST['tb_no_guest']
            tb_date_c = request.POST['tb_date']
            tb_time = request.POST['tb_time']
            table_type_s = request.POST['table_type']
            tb_choose = request.POST['tb_choose']
            u_id = request.session['u_id']
            # print(type(tb_date))
            # print(type(today))
            tb_no_guest = int(tb_no_guest_s)
            table_type = int(table_type_s)
            tb_date = datetime.strptime(tb_date_c, '%Y-%m-%d').date()
            if tb_no_guest > table_type:
                messages.success(
                    request, 'Table type smaller than recruitment Member....')
                return redirect('table')
            elif tb_date < today:
                messages.success(request, "Table can'n book in past....")
                return redirect('table')
            else:
                tb = Table_Booking.objects.all()
                tt = int(table_type)
                t = 0
                for i in tb:
                    ed = str(tb_date)
                    dd = str(i.tb_date)
                    et = str(tb_time)
                    dt = str(i.tb_time)
                    if ed == dd and et == dt:
                        t = t + i.table_type
                        # print(t)
                if t <= 50:
                    o = t + tt
                    if o <= 50:
                        tb = Table_Booking(
                            tb_name=tb_name,
                            tb_contact=tb_contact,
                            tb_email=tb_email,
                            tb_no_guest=tb_no_guest,
                            tb_date=tb_date,
                            tb_time=tb_time,
                            table_type=table_type,
                            tb_choose=tb_choose,
                            u_id=u_id)
                        tb.save()
                    else:
                        messages.success(request, 'Table is Alreddy booked')
                        return render(request, 'table.html')
                else:
                    tb = Table_Booking(
                        tb_name=tb_name,
                        tb_contact=tb_contact,
                        tb_email=tb_email,
                        tb_no_guest=tb_no_guest,
                        tb_date=tb_date,
                        u_id=u_id,
                        tb_time=tb_time,
                        table_type=table_type,
                        tb_choose=tb_choose)
                    tb.save()
            messages.success(request, 'Table is booked for you')
            return redirect('home')
        return render(request, 'table.html', {'admin': admin})
    else:
        return redirect('login_page')


def table_booking_detail(request):
    if request.session.get('admin_id'):
        tb = Table_Booking.objects.all()
        return render(request, "table_booking_detail.html", {'tb': tb})
    else:
        return redirect('admin_login')


def table_booking_detail_today(request):
    today = date.today()
    tb = Table_Booking.objects.filter(tb_date=today)
    return render(request, "table_booking_detail_today.html", {'tb': tb})


def edit_tb(request, tb_id):
    if request.session.get('admin_id'):
        tb = Table_Booking.objects.get(tb_id=tb_id)
        return render(request, "update_table.html", {'data_tb': tb})
    else:
        return redirect('admin_login')


def update_tb(request, tb_id):
    if request.session.get('admin_id'):
        tb = Table_Booking.objects.get(tb_id=tb_id)
        tb.tb_name = request.POST['tb_name']
        tb.tb_contact = request.POST['tb_contact']
        tb.tb_email = request.POST['tb_email']
        tb.tb_no_guest = request.POST['tb_no_guest']
        tb.tb_date = request.POST['tb_date']
        tb.tb_time = request.POST['tb_time']
        tb.table_type = request.POST['table_type']
        tb.tb_choose = request.POST['tb_choose']
        tb.save()
        return redirect('table_booking_detail')
    else:
        return redirect('admin_login')


def delete_tb(request, tb_id):
    if request.session.get('admin_id'):
        tb = Table_Booking.objects.get(tb_id=tb_id)
        tb.delete()
        return redirect('table_booking_detail')
    else:
        return redirect('admin_login')


# HALL BOOKING


def hall_booking(request):
    hb = Hall_Booking.objects.all()
    user = UsersModel.objects.all()
    return render(request, "hall_booking.html", {'hb': hb, 'user': user})


def hall_booking_today(request):
    today = date.today()
    hb = Hall_Booking.objects.filter(date=today)
    user = UsersModel.objects.all()
    return render(request, "hall_booking_today.html", {'hb': hb, 'user': user})


# Admin


def control_admin(request):
    return render(request, "admin.html")


def dashboard(request):
    if request.session.get('admin_id'):
        today = date.today()
        customer = UsersModel.objects.count()
        events = Event.objects.filter(event_date_time=today)
        order = Order.objects.count()
        o = Order.objects.all()
        hbc = Hall_Booking.objects.filter(date=today)
        table = Table_Booking.objects.filter(tb_date=today)
        hb = hbc.count()
        tb = table.count()
        event = events.count()
        fc = Food_category.objects.count()
        fi = FoodItem.objects.count()
        new_order = 0
        for i in o:
            if 'Pending' == i.order_status:
                new_order = new_order+1
        on_delevery = 0
        for i in o:
            if 'Confirm' == i.order_status:
                on_delevery = on_delevery+1
        nothing = {'fi': fi, 'fc': fc, 'tb': tb, 'customer': customer, 'event': event,
                   'order': order, 'on_delevery': on_delevery, 'new_order': new_order, 'hb': hb}
        return render(request, "dashboard.html", nothing)
    else:
        return redirect('admin_login')


def admin_table(request):
    if request.session.get('admin_id'):
        admin = Admin.objects.all()
        return render(request, "admin_table.html", {'admin': admin})
    else:
        return redirect('admin_login')


def add_admin(request):
    if request.session.get('admin_id'):
        if request.method == "POST":
            admin_name = request.POST['admin_name']
            admin_password = request.POST['admin_password']
            email_id = request.POST['email_id']
            contact_number = request.POST['contact_number']
            admin = Admin(
                admin_name=admin_name,
                admin_password=admin_password,
                email_id=email_id,
                contact_number=contact_number)
            admin.save()
            return redirect('admin_table')
        return render(request, 'add_admin.html')
    else:
        return redirect('admin_login')


def edit_admin(request, id):
    if request.session.get('admin_id'):
        admin = Admin.objects.get(admin_id=id)
        return render(request, "update_admin.html", {'data_admin': admin})
    else:
        return redirect('admin_login')


def update_admin(request, id):
    if request.session.get('admin_id'):
        admin = Admin.objects.get(admin_id=id)
        admin.admin_name = request.POST['admin_name']
        admin.admin_password = request.POST['admin_password']
        admin.email_id = request.POST['email_id']
        admin.contact_number = request.POST['contact_number']
        admin.save()
        return redirect('admin_table')
    else:
        return redirect('admin_login')


def delete_admin(request, id):
    if request.session.get('admin_id'):
        a_c = Admin.objects.count()
        if a_c > 1:
            admin = Admin.objects.get(admin_id=id)
            admin.delete()
            return redirect('admin_table')
        else:
            messages.success(request, "You can not delete all admin")
            return redirect('admin_table')
    else:
        return redirect('admin_login')


# Event


def event_display(request):
    if request.session.get('admin_id'):
        nothing = Event.objects.all()
        user = UsersModel.objects.all()
        return render(request, "event_display.html", {'nothing': nothing, 'user': user})
    else:
        return redirect('admin_login')


def event_display_today(request):
    today = date.today()
    nothing = Event.objects.filter(event_date_time=today)
    user = UsersModel.objects.all()
    return render(request, "event_display_today.html", {'nothing': nothing, 'user': user})


def add_event(request):
    if request.session.get('u_id') or request.session.get('admin_id'):
        u_name = request.session['u_id']
        user = UsersModel.objects.get(u_id=u_name)
        if request.method == "POST":
            alt_contactno = request.POST['alt_contactno']
            event_what = request.POST['event_what']
            event_date_time = request.POST['event_date_time']
            delivery_add = request.POST['delivery_add']
            number_of_person = request.POST['number_of_person']
            event = Event(
                alt_contactno=alt_contactno,
                event_what=event_what,
                event_date_time=event_date_time,
                delivery_add=delivery_add,
                u_id=u_name,
                number_of_person=number_of_person)
            event.save()
            request.session['event_id'] = event.event_id
            event_id = request.session.get('event_id')
            print(event_id)
            return redirect('packages')
        return render(request, 'add_event.html', {'u_id': u_name, 'user': user})
    else:
        return redirect('login_page')


def add_event_hotel(request):
    if request.session.get('u_id') or request.session.get('admin_id'):
        u_name = request.session['u_id']
        user = UsersModel.objects.get(u_id=u_name)
        if request.method == "POST":
            alt_contactno = request.POST['alt_contactno']
            event_what = request.POST['event_what']
            event_date_time = request.POST['event_date_time']
            delivery_add = "Patel Parotha House"
            number_of_person = request.POST['number_of_person']
            S_time = request.POST['S_time']
            E_time = request.POST['E_time']
            event = Event.objects.all()
            hall_is = 0
            for i in event:
                ed = str(event_date_time)
                dd = str(i.event_date_time)
                print(ed)
                print(dd)
                if ed == dd and i.delivery_add == 'Patel Parotha House':
                    hall_is = 1
            print(hall_is)
            if hall_is == 0:
                event = Event(
                    alt_contactno=alt_contactno,
                    event_what=event_what,
                    event_date_time=event_date_time,
                    delivery_add=delivery_add,
                    u_id=u_name,
                    number_of_person=number_of_person)
                event.save()
                request.session['event_id'] = event.event_id
                event_id = request.session.get('event_id')
                hb = Hall_Booking(
                    date=event_date_time,
                    start_time=S_time,
                    u_id=u_name,
                    end_time=E_time,
                    event_id=event_id)
                hb.save()
                messages.error(
                    request, "Hall booked for you, Please select your package")
                return redirect('packages')
            else:
                messages.error(request, "Hall is alredy booked")
                return redirect('home')
        return render(request, 'add_event_hotel.html', {'u_id': u_name, 'user': user})
    else:
        return redirect('login_page')


def edit_event(request, id):
    if request.session.get('admin_id'):
        event = Event.objects.get(event_id=id)
        return render(request, "update_event.html", {'data_event': event})
    else:
        return redirect('admin_login')


def update_event(request, id):
    if request.session.get('admin_id'):
        event = Event.objects.get(event_id=id)
        event.event_what = request.POST['event_what']
        event.event_date_time = request.POST['event_date_time']
        event.delivery_add = request.POST['delivery_add']
        event.number_of_person = request.POST['number_of_person']
        event.alt_contactno = request.POST['alt_contactno']
        event.save()
        return redirect('event_display')
    else:
        return redirect('admin_login')


def delete_event(request, id):
    if request.session.get('admin_id'):
        event = Event.objects.get(event_id=id)
        event.delete()
        return redirect('event_display')
    else:
        return redirect('admin_login')


# SERVICES


def services(request):
    admin = request.session.get('admin_id')
    try:
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "services.html", {'admin': admin, 'u_id': u_id, 'user': user})
    except:
        return render(request, "services.html", {'admin': admin})


def wedding(request):
    try:
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "wedding.html", {'u_id': u_id, 'user': user})
    except:
        return render(request, "wedding.html",)


def corporate(request):
    try:
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "corporate.html", {'u_id': u_id, 'user': user})
    except:
        return render(request, "corporate.html")


def socials(request):
    try:
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "socials.html", {'u_id': u_id, 'user': user})
    except:
        return render(request, "socials.html")


def festivals(request):
    try:
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "festivals.html", {'u_id': u_id, 'user': user})
    except:
        return render(request, "festivals.html")


def private_parties(request):
    try:
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "private_parties.html", {'u_id': u_id, 'user': user})
    except:
        return render(request, "private_parties.html")


def packages(request):
    u_id = request.session.get('u_id')
    user = UsersModel.objects.get(u_id=u_id)
    return render(request, "packages.html", {'u_id': u_id, 'user': user})


def packagesS(request):
    fi = Event_menu_item.objects.all()
    sweets = Event_menu_item.objects.filter(emi_category='sweet')
    u_id = request.session.get('u_id')
    user = UsersModel.objects.get(u_id=u_id)
    return render(request, "package300.html", {'fi': fi, 'sweets': sweets, 'u_id': u_id, 'user': user})


def packagesM(request):
    fi = Event_menu_item.objects.all()
    u_id = request.session.get('u_id')
    user = UsersModel.objects.get(u_id=u_id)
    return render(request, "package400.html", {'fi': fi, 'u_id': u_id, 'user': user})


def packagesL(request):
    u_id = request.session.get('u_id')
    user = UsersModel.objects.get(u_id=u_id)
    fi = Event_menu_item.objects.all()
    return render(request, "package550.html", {'fi': fi, 'u_id': u_id, 'user': user})


def packagesXL(request):
    u_id = request.session.get('u_id')
    user = UsersModel.objects.get(u_id=u_id)
    fi = Event_menu_item.objects.all()
    return render(request, "package800.html", {'fi': fi, 'u_id': u_id, 'user': user})


# Order Menu Cart Section


def order(request):
    if request.session.get('admin_id'):
        o = Order.objects.all()
        order = reversed(o)
        user = UsersModel.objects.all()
        return render(request, "order.html", {'order': order, 'user': user})
    else:
        return redirect('admin_login')


def cart(request):
    if request.session.get('u_id'):
        previous_url = request.META.get('HTTP_REFERER', '/')
        name = request.session['u_id']
        if request.method == 'POST':
            f_id = request.POST['f_item']
            cart = request.session.get('cart', {})
            order_id = request.session.get('order_id')
            if order_id == None:
                u_id = name
                address = 'u_address'
                mobile_no = 'contact'
                order_date = date.today()
                order_time = datetime.now().time()
                # order_time = datetime.strptime(order_time, '%I:%M %p').time()
                o_time = "10:00 AM"
                c_time = "11:00 PM"
                o_time = datetime.strptime(o_time, '%I:%M %p').time()
                c_time = datetime.strptime(c_time, '%I:%M %p').time()
                if o_time >= order_time or order_time >= c_time:
                    messages.success(
                        request, 'Apologies, our restaurant is currently closed. Please do visit us again during our opening hours....')
                    return redirect(previous_url)
                else:
                    order = Order(
                        u_id=u_id,
                        address=address,
                        mobile_no=mobile_no,
                        order_date=order_date,
                        order_time=order_time)
                    order.save()
                    order_id_d = Order.objects.all()
                    for i in order_id_d:
                        if (u_id == i.u_id and order_date == i.order_date and order_time == i.order_time):
                            request.session['order_id'] = i.order_id
            if f_id in cart:
                cart[f_id] += 1
            else:
                cart[f_id] = 1
            request.session['cart'] = cart
        return redirect(previous_url)
    else:
        return redirect('login_page')


def order_item(request):
    if request.session.get('u_id'):
        cart = request.session['cart']
        order_d = Order_Details.objects.all()
        return redirect('menu', {'order_d': order_d, 'cart': cart})
    else:
        return redirect('login_page')


def cart_item(request):
    cart = request.session.get('cart')
    fc = Food_category.objects.all()
    fi = FoodItem.objects.all()
    if cart != None:
        cart_int = [int(i) for i in cart]
        return render(request, "cart_item.html", {'fc': fc, 'fi': fi, 'cart_int': cart_int})
    return redirect('menu')


def atl_cont_out(request):
    uid = request.session['u_id']
    user = UsersModel.objects.get(u_id=uid)
    pincode = user.u_pin_code
    sa = Servise_area.objects.all()
    return render(request, "atl_cont_out.html", {'user': user, 'uid': uid, 'sa': sa})


def atl_cont(request):
    uid = request.session['u_id']
    user = UsersModel.objects.get(u_id=uid)
    pincode = user.u_pin_code
    try:
        pin_codes = Servise_area.objects.get(pin_code=pincode)
        if pin_codes:
            return render(request, "atl_cont.html", {'user': user, 'uid': uid, })
    except:
        messages.success(request, 'This Area is not in service....')
        sa = Servise_area.objects.all()
        return render(request, "atl_cont_out.html", {'user': user, 'uid': uid, 'sa': sa})


def alt_form(request):
    u_idl = request.session['u_id']
    u_id = int(u_idl)
    if request.method == "POST":
        a = request.session.get('order_id')
        order = Order.objects.get(order_id=a)
        order.u_id = u_id
        order.address = request.POST['alt_add']
        order.mobile_no = request.POST['alt_cont']
        order.order_date = date.today()
        order.order_time = datetime.now().time()
        order.save()
        id = order.order_id
        # order_details_pdf(request,id)
        request.session['order_id'] = None
        messages.success(request, 'Order is booked for you')
        return redirect('order_details',id)


def order_details_pdf(request, id):
    u_id = request.session.get('u_id')
    order_item = Order_Details.objects.all()
    a = Order.objects.get(order_id = id)
    user = UsersModel.objects.get(u_id=u_id)
    template_path = 'order_details_pdf.html'
    context = {'order': order_item, 'a': a,'u_id':u_id,'user':user}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def status(request, id):
    previous_url = request.META.get('HTTP_REFERER', '/')
    order = Order.objects.get(order_id=id)
    if request.method == "POST":
        order.order_status = request.POST['order_status']
        order.save()
    return redirect(previous_url)


def cart_item_detail(request):
    cart = request.session['cart']
    order_id = request.session['order_id']
    t_p = 0
    if request.method == "POST":
        for u in cart:
            order_id = order_id
            fi_id = request.POST['fi_id'+u]
            fi_name = request.POST['fi_name' + u]
            quantity = request.POST['quantity'+u]
            price = request.POST['price'+u]
            t_price = request.POST['t_price'+u]
            order_D = Order_Details(
                order_id=order_id,
                fi_id=fi_id,
                fi_name=fi_name,
                quantity=quantity,
                price=price,
                t_price=t_price,)
            t_p = int(t_price) + t_p
            order_D.save()
        t_items = len(cart)
        order = Order.objects.get(order_id=order_id)
        order.t_p = t_p
        order.items = t_items
        order.save()
        del request.session['cart']
        return redirect('atl_cont')


def cancel_order(request):
    co = request.session.get('order_id')
    order = Order.objects.get(order_id=co)
    order.delete()
    return redirect('home')


def remove_cart_item(request, id):
    cart = request.session['cart']
    a = str(id)
    cart.pop(a)
    request.session['cart'] = cart
    return redirect('cart_item')


def order_details(request, id):
    if request.session.get('u_id'):
        order = Order_Details.objects.all()
        a = id
        u_id = request.session.get('u_id')
        user = UsersModel.objects.get(u_id=u_id)
        return render(request, "order_details.html", {'order': order, 'a': a, 'u_id': u_id, 'user': user})
    else:
        return redirect('login_page')


def order_d(request):
    order_d = Order_Details.objects.all()
    return render(request, "order_d.html", {'order_d': order_d})


def order_d(request, id):
    order = Order_Details.objects.all()
    a = id
    print(a)
    return render(request, "order_d.html", {'order': order, 'a': a})


def panding_order(request):
    o = Order.objects.all()
    order = reversed(o)
    user = UsersModel.objects.all()
    return render(request, "panding_order.html", {'order': order, 'user': user})


def on_delivery(request):
    user = UsersModel.objects.all()
    o = Order.objects.all()
    order = reversed(o)
    return render(request, "on_delivery.html", {'order': order, 'user': user})


def add_event_menu_category(request):
    if request.session.get('admin_id'):
        if request.method == "POST":
            emc_name = request.POST['emc_name']
            emc_description = request.POST['emc_description']
            emc = Event_menu_category(
                emc_name=emc_name,
                emc_description=emc_description)
            emc.save()
            return redirect('event_menu_category')
        return render(request, 'add_event_menu_category.html')
    else:
        return redirect('admin_login')


def event_menu_category(request):
    if request.session.get('admin_id'):
        emc = Event_menu_category.objects.all()
        return render(request, "event_menu_category.html", {'emc': emc})
    else:
        return redirect('admin_login')


def edit_emc(request, emc_id):
    if request.session.get('admin_id'):
        emc = Event_menu_category.objects.get(emc_id=emc_id)
        return render(request, "updet_event_menu_category.html", {'data_emc': emc})
    else:
        return redirect('admin_login')


def update_emc(request, emc_id):
    if request.session.get('admin_id'):
        emc = Event_menu_category.objects.get(emc_id=emc_id)
        emc.emc_name = request.POST['emc_name']
        emc.emc_description = request.POST['emc_description']
        emc.save()
        return redirect('event_menu_category')
    else:
        return redirect('admin_login')


def delete_emc(request, emc_id):
    if request.session.get('admin_id'):
        emc = Event_menu_category.objects.get(emc_id=emc_id)
        emc.delete()
        return redirect('event_menu_category')
    else:
        return redirect('admin_login')


def event_menu_item_detail(request):
    if request.session.get('admin_id'):
        emi = Event_menu_item.objects.all()
        return render(request, "event_menu_item.html", {'emi': emi})
    else:
        return redirect('admin_login')


def similar_efi(request, efc_id):
    # print(fc_id)
    emc = Event_menu_category.objects.get(emc_id=efc_id)
    cat = emc.emc_name
    emi = Event_menu_item.objects.filter(emi_category=cat)
    return render(request, "similar_efi.html", {'emi': emi})


def add_event_menu_item(request):
    if request.session.get('admin_id'):
        emc = Event_menu_category.objects.all()
        if request.method == "POST":
            emi_name = request.POST['emi_name']
            categories = request.POST['categories']
            emi_price = request.POST['emi_price']
            emi_lavel = request.POST['emi_lavel']
            emi = Event_menu_item(
                emi_name=emi_name,
                emi_category=categories,
                emi_price=emi_price,
                emi_lavel=emi_lavel)
            emi.save()
            return redirect('event_menu_item_detail')
        return render(request, 'add_event_menu_item.html', {'emc': emc})
    else:
        return redirect('admin_login')


def edit_emi(request, emi_id):
    if request.session.get('admin_id'):
        emi = Event_menu_item.objects.get(emi_id=emi_id)
        emc = Event_menu_category.objects.all()
        return render(request, "updet_event_menu_item.html", {'data_emi': emi, 'emc': emc})
    else:
        return redirect('admin_login')


def update_emi(request, emi_id):
    if request.session.get('admin_id'):
        emi = Event_menu_item.objects.all()
        emi = Event_menu_item.objects.get(emi_id=emi_id)
        emi.emi_name = request.POST['emi_name']
        emi.emi_price = request.POST['emi_price']
        emi.emi_category = request.POST['emi_category']
        emi.emi_lavel = request.POST['emi_lavel']
        emi.save()
        return redirect('event_menu_item_detail')
    else:
        return redirect('admin_login')


def delete_emi(request, emi_id):
    if request.session.get('admin_id'):
        emi = Event_menu_category.objects.get(emi_id=emi_id)
        emi.delete()
        return redirect('event_menu_item_detail')
    else:
        return redirect('admin_login')


def event_menu(request):
    if request.method == "POST":
        num_values = len(request.POST)
        u_id = request.session.get('u_id')
        event_id = request.session.get('event_id')
        e_price = 0
        for i in range(1, num_values+1):
            l = str(i)
            number = request.POST['item'+l]
            itme = Event_menu_item.objects.filter(emi_id=number)
            for i in itme:
                u_id = u_id
                event_id = event_id
                emi_id = i.emi_id
                emi_name = i.emi_name
                emi_peice = i.emi_price
                emi_category = i.emi_category
                e_price = e_price + emi_peice
                em = Event_menu(
                    emi_name=emi_name,
                    u_id=u_id,
                    emi_peice=emi_peice,
                    emi_id=emi_id,
                    event_id=event_id,
                    emi_category=emi_category)
                em.save()
        event = Event.objects.get(event_id=event_id)
        event.p_price = e_price
        event.a_price = e_price
        event.save()
        messages.success(request, 'Menu is booked for you')
        request.session['event_id'] = None
        return redirect('home')


def menu_details(request, items):
    m_items = Event_menu.objects.all()
    return render(request, "menu_details.html", {'m_items': m_items, 'items': items})


def user_menu_details(request, items):
    m_items = Event_menu.objects.all()
    u_id = request.session['u_id']
    user = UsersModel.objects.get(u_id=u_id)

    return render(request, "user_menu_details.html", {'m_items': m_items, 'items': items, 'user': user, 'u_id': u_id})


def user_order(request):
    u_id = request.session['u_id']
    name = request.session['name']
    contact = request.session['contact']
    user_data = UsersModel.objects.filter(contact=contact)
    p_order = Order.objects.filter(u_id=u_id, order_status='Pending')
    c_order = Order.objects.filter(u_id=u_id, order_status='Confirm')
    d_order = Order.objects.filter(u_id=u_id, order_status='Delivere')
    tb = Table_Booking.objects.filter(u_id=u_id)
    user = UsersModel.objects.get(u_id=u_id)
    event = Event.objects.filter(u_id=u_id)
    return render(request, "user_order.html", {'user': user, 'tb': tb, 'p_order': p_order, 'c_order': c_order, 'd_order': d_order, 'name': name, 'u_id': u_id, 'event': event, 'user_date': user_data})


def service_area(request):
    sa = Servise_area.objects.all()
    return render(request, 'service_area.html', {'sa': sa})


def add_sa(request):
    if request.session.get('admin_id'):
        if request.method == "POST":
            sa_name = request.POST['sa_name']
            pin_code = request.POST['pin_code']
            sa = Servise_area(
                sa_name=sa_name,
                pin_code=pin_code
            )
            sa.save()
            return redirect('service_area')
        return render(request, 'add_sa.html')
    else:
        return redirect('admin_login')


def edit_sa(request, id):
    if request.session.get('admin_id'):
        sa = Servise_area.objects.get(sa_id=id)
        return render(request, "updet_sa.html", {'sa': sa})
    else:
        return redirect('admin_login')


def update_sa(request, id):
    sa = Servise_area.objects.get(sa_id=id)
    sa.sa_name = request.POST['sa_name']
    sa.pin_code = request.POST['pin_code']
    sa.save()
    return redirect('service_area')


def delete_sa(request, sa_id):
    if request.session.get('admin_id'):
        sa = Servise_area.objects.get(sa_id=sa_id)
        sa.delete()
        return redirect('service_area')
    else:
        return redirect('admin_login')


# PDF


def render_pdf_view(request):
    # Import data teble
    Data = Data.objectes.all()
    template_path = 'file_name.html'
    context = {'Data': 'Data'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
