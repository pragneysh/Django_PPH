from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                path('login_admin', views.login_admin, name='login_admin'),
                path('admin_login', views.admin_login, name='admin_login'),
                path('admin_logout', views.admin_logout, name='admin_logout'),

                path('admin_base', views.admin_base, name='admin_base'),

                path('', views.home, name='home'),
                path('home', views.home, name='home'),

                path('table', views.table, name='table'),
                path('menu', views.menu, name='menu'),
                path('about', views.about, name='about'),
                path('dishes', views.dishes, name='dishes'),

                path('control_admin', views.control_admin, name='control_admin'),

                path('login_page', views.login_page, name='login_page'),
                path('adduser', views.registeruser, name='adduser'),
                path('loginuser', views.loginuser, name='loginuser'),
                path('logout', views.logout, name='logout'),

                path('user_account', views.user_account, name='user_account'),
                path('edit_form/<int:id>', views.edit_form, name="edit_form"),
                path('update_user/<int:id>', views.update_user, name="update_user"),
                path('edit_image/<int:id>', views.edit_image, name="edit_image"),              
                path('update_image/<int:id>', views.update_image, name="update_image"),

                path('customer_detail', views.customer_detail, name='customer_detail'),
                path('delete_data/<int:id>', views.delete_data, name="delete_data"),

                path('createitem', views.createitem, name='createitem'),
                path('food_Item_detail', views.food_Item_detail, name='food_Item_detail'),
                path('food_Item_detail_pdf', views.food_Item_detail_pdf, name='food_Item_detail_pdf'),
                path('edit_fi/<int:fi_id>', views.edit_fi, name="edit_fi"),
                path('edit_food_image/<int:id>', views.edit_food_image, name="edit_food_image"),  
                path('update_food_image/<int:id>', views.update_food_image, name="update_food_image"),
                path('update_fi/<int:fi_id>', views.update_fi, name="update_fi"),
                path('delete_fi/<int:fi_id>', views.delete_fi, name="delete_fi"),

                path('food_category', views.food_category, name='food_category'),
                path('add_food_category', views.add_food_category, name='add_food_category'),
                path('edit_fc/<int:fc_id>', views.edit_fc, name="edit_fc"),
                path('update_fc/<int:fc_id>', views.update_fc, name="update_fc"),
                path('delete_fc/<int:fc_id>', views.delete_fc, name="delete_fc"),
                path('similar_fi/<int:fc_id>', views.similar_fi, name='similar_fi'),

                path('table_booking_detail', views.table_booking_detail,
                        name='table_booking_detail'),
                path('table_booking_detail_today', views.table_booking_detail_today,
                        name='table_booking_detail_today'),
                path('table_booking', views.table_booking, name='table_booking'),
                path('edit_tb/<int:tb_id>', views.edit_tb, name="edit_tb"),
                path('update_tb/<int:tb_id>', views.update_tb, name="update_tb"),
                path('delete_tb/<int:tb_id>', views.delete_tb, name="delete_tb"),

                path('display', views.display, name='display'),
                path('update', views.update, name='update'),
                path('add', views.add, name='add'),

                path('admin_table', views.admin_table, name='admin_table'),
                path('add_admin', views.add_admin, name='add_admin'),
                path('edit_admin/<int:id>', views.edit_admin, name="edit_admin"),
                path('update_admin/<int:id>', views.update_admin, name="update_admin"),
                path('delete_admin/<int:id>', views.delete_admin, name="delete_admin"),

                path('services', views.services, name='services'),
                path('wedding', views.wedding, name='wedding'),
                path('corporate', views.corporate, name='corporate'),
                path('socials', views.socials, name='socials'),
                path('festivals', views.festivals, name='festivals'),
                path('private_parties', views.private_parties, name='private_parties'),

                path('packages', views.packages, name='packages'),
                path('packagesS', views.packagesS, name='packagesS'),
                path('packagesM', views.packagesM, name='packagesM'),
                path('packagesL', views.packagesL, name='packagesL'),
                path('packagesXL', views.packagesXL, name='packagesXL'),

                path('order', views.order, name='order'),
                path('panding_order', views.panding_order, name='panding_order'),
                path('on_delivery', views.on_delivery, name='on_delivery'),
                path('cart', views.cart, name='cart'),
                path('cart_item', views.cart_item, name='cart_item'),
                path('cart_item_detail', views.cart_item_detail, name='cart_item_detail'),
                path('order_item', views.order_item, name='order_item'),
                path('user_order', views.user_order, name='user_order'),

                path('event_display', views.event_display, name='event_display'),
                path('event_display_today', views.event_display_today, name='event_display_today'),

                path('add_event', views.add_event, name='add_event'),
                path('add_event_hotel', views.add_event_hotel, name='add_event_hotel'),
                path('edit_event/<int:id>', views.edit_event, name="edit_event"),
                path('update_event/<int:id>', views.update_event, name="update_event"),
                path('delete_event/<int:id>', views.delete_event, name="delete_event"),

                path('event_menu_category', views.event_menu_category, name='event_menu_category'),
                path('add_event_menu_category', views.add_event_menu_category, name='add_event_menu_category'),
                path('edit_emc/<int:emc_id>', views.edit_emc, name="edit_emc"),
                path('update_emc/<int:emc_id>', views.update_emc, name="update_emc"),
                path('delete_emc/<int:emc_id>', views.delete_emc, name="delete_emc"),

                path('event_menu_item_detail', views.event_menu_item_detail, name='event_menu_item_detail'),
                path('add_event_menu_item', views.add_event_menu_item, name='add_event_menu_item'),
                path('edit_emi/<int:emi_id>', views.edit_emi, name="edit_emi"),
                path('update_emi/<int:emi_id>', views.update_emi, name="update_emi"),
                path('delete_emi/<int:emi_id>', views.delete_emi, name="delete_emi"),
                path('similar_efi/<int:efc_id>', views.similar_efi, name='similar_efi'),

                path('atl_cont', views.atl_cont, name='atl_cont'),
                path('atl_cont_out', views.atl_cont_out, name='atl_cont_out'),
                path('alt_form', views.alt_form, name='alt_form'),
                path('status/<int:id>', views.status, name='status'),

                path('order_details/<int:id>', views.order_details, name='order_details'),
                path('order_details_pdf/<int:id>', views.order_details_pdf, name='order_details_pdf'),

                path('order_d/<int:id>', views.order_d, name='order_d'),
                path('remove_cart_item/<int:id>',
                        views.remove_cart_item, name='remove_cart_item'),
                path('cancel_order', views.cancel_order, name="cancel_order"),

                path('dashboard', views.dashboard, name='dashboard'),

                path('event_menu', views.event_menu, name='event_menu'),
                path('menu_details/<int:items>', views.menu_details, name='menu_details'),
                path('user_menu_details/<int:items>', views.user_menu_details, name='user_menu_details'),

                path('hall_booking', views.hall_booking, name='hall_booking'),
                path('hall_booking_today', views.hall_booking_today, name='hall_booking_today'),

                path('add_sa', views.add_sa, name='add_sa'),
                path('service_area', views.service_area, name='service_area'),
                path('edit_sa/<int:id>', views.edit_sa, name="edit_sa"),
                path('update_sa/<int:id>', views.update_sa, name="update_sa"),
                path('delete_sa/<int:sa_id>', views.delete_sa, name="delete_sa"),








]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
