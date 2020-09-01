from django import template
from productos.models import Product


register = template.Library()


@register.simple_tag
def product_price_cop(pk):
  product = Product.objects.get(pk=pk)

  usd_price_in_cop_day = 3450
  return product.product_price_usd * usd_price_in_cop_day


@register.simple_tag
def product_price_bs(pk):
  product = Product.objects.get(pk=pk)

  usd_price_in_cop_bs = 280000

  return product.product_price_usd * usd_price_in_cop_bs