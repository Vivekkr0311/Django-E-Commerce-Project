# Generated by Django 3.0.8 on 2020-09-17 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200917_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watch_list',
            old_name='product_name',
            new_name='product_ID',
        ),
        migrations.RenameField(
            model_name='watch_list',
            old_name='user_name',
            new_name='user_ID',
        ),
    ]
