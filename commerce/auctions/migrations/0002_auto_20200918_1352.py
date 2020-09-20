# Generated by Django 3.0.8 on 2020-09-18 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=64)),
                ('link', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.IntegerField()),
                ('owner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]