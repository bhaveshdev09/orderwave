# Generated by Django 4.2.8 on 2024-01-04 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aggregator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Aggregator Name')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='deleted')),
            ],
            options={
                'verbose_name': 'Aggregator',
                'verbose_name_plural': 'Aggregators',
                'managed': True,
            },
        ),
    ]