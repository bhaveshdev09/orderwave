# Generated by Django 4.2.8 on 2024-01-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_train_name_bill_train_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='payment_type',
            field=models.CharField(choices=[('cash', 'cash'), ('upi', 'upi')], default='upi', max_length=20),
        ),
    ]
