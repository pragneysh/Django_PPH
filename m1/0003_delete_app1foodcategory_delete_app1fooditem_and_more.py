# Generated by Django 4.1 on 2022-12-29 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_admin_app1foodcategory_app1fooditem_app1tablebooking_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='App1FoodCategory',
        ),
        migrations.DeleteModel(
            name='App1Fooditem',
        ),
        migrations.DeleteModel(
            name='App1TableBooking',
        ),
        migrations.DeleteModel(
            name='App1Usersmodel',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='DjangoSite',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='HallBooking',
        ),
        migrations.DeleteModel(
            name='PartyOrder',
        ),
        migrations.AlterModelOptions(
            name='admin',
            options={},
        ),
    ]