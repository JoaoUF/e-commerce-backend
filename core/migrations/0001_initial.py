# Generated by Django 5.0.3 on 2024-03-23 21:47

import django_extensions.db.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('a5362dfe-1d73-4e1f-a4c1-cfd6f6ee80f3'), primary_key=True, serialize=False, verbose_name='id')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('title', models.CharField(db_column='title', max_length=200, verbose_name='Titulo del producto')),
                ('price', models.FloatField(db_column='price', verbose_name='Precio del producto')),
                ('discountPrice', models.FloatField(db_column='discount_price', verbose_name='Descuento del producto')),
                ('category', models.CharField(db_column='category', max_length=200, verbose_name='Categoria del producto')),
                ('description', models.TextField(db_column='description', verbose_name='Descripcion del producto')),
                ('image', models.CharField(db_column='image', verbose_name='image')),
            ],
            options={
                'db_table': 'MAE_PRODUCT',
            },
        ),
    ]