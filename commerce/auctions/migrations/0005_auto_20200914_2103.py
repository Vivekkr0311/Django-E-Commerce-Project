# Generated by Django 3.0.8 on 2020-09-14 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200914_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='active_listing',
            old_name='name_owner',
            new_name='owner_name',
        ),
    ]