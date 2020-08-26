from django.db import models

# Create your models here.

class Product(models.Model):
  product_name = models.CharField(max_length=255)
  product_description = models.CharField(max_length=255)
  product_price_bs = models.IntegerField(default=0)
  product_price_cop = models.IntegerField(default=0)
  product_price_usd = models.IntegerField(default=0)

  def __str__(self):

    return self.product_name

