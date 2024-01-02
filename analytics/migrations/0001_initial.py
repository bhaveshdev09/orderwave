# Generated by Django 4.2.8 on 2024-01-01 15:55

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('vendors', '0001_initial'),
        ('purchase_orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyCustomer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('customers.customer',),
        ),
        migrations.CreateModel(
            name='ProxyPurchseOrder',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('purchase_orders.purchaseorder',),
        ),
        migrations.CreateModel(
            name='ProxyVendor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('vendors.vendor',),
        ),
    ]