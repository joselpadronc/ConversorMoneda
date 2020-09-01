from django.db import models

# Create your models here.

class Product(models.Model):
  product_name = models.CharField(max_length=255)
  product_description = models.CharField(max_length=255)
  product_price = models.IntegerField(default=0)

  def __str__(self):

    return self.product_name


class Currency(models.Model):
  currency_name = models.CharField(max_length=255)
  currency_price = models.IntegerField(default=0)

  def __str__(self):

    return self.id, self.currency_name