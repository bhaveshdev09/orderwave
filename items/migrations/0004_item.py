# Generated by Django 4.2.8 on 2023-12-22 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20231222_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('base_price', models.FloatField()),
                ('tax', models.FloatField(default=18, editable=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='items.category')),
                ('operation_hour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='items.operatinghour')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='items.section')),
            ],
        ),
    ]