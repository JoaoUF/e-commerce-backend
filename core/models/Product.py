from django.db import models
from utils.model import Model
from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Product(ActivatorModel, TimeStampedModel, Model):
    title = models.CharField(
        verbose_name='Titulo del producto',
        db_column='title',
        max_length=200,
    )
    price = models.FloatField(
        verbose_name='Precio del producto',
        db_column='price',
    )
    discountPrice = models.FloatField(
        verbose_name='Descuento del producto',
        db_column='discount_price',
    )
    category = models.CharField(
        verbose_name='Categoria del producto',
        db_column='category',
        max_length=200
    )
    description = models.TextField(
        verbose_name='Descripcion del producto',
        db_column='description',
    )
    image = models.CharField(
        verbose_name='image',
        db_column='image',
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'MAE_PRODUCT'
