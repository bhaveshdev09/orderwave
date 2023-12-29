# Generated by Django 4.2.8 on 2023-12-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('units', models.CharField(choices=[('kgs', 'Kilograms'), ('ltrs', 'Liters'), ('pcs', 'Pieces'), ('units', 'Units')], default='units', max_length=5)),
                ('price', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
