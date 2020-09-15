# Generated by Django 3.0.8 on 2020-09-15 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20200915_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='active_listing',
            name='owner_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
