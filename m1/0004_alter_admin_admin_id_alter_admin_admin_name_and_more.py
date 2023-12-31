# Generated by Django 4.1 on 2022-12-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_delete_app1foodcategory_delete_app1fooditem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='admin_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='admin',
            name='admin_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='admin',
            name='admin_password',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='admin',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='admin',
            name='email_id',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='admin',
            table=None,
        ),
    ]
