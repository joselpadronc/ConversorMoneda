from django.shortcuts import render
from django.http import HttpResponse

# Models
from .models import Product, Currency


# Template Tags
from .templatetags.product_tag import product_price_bs, product_price_cop
# Create your views here.


# def conversor(request):
#   template_name = 'index.html'
#   products = Product.objects.all()

#   for product_price in products:
#     product_price_in_usd = product_price.product_price_usd

#     usd_price_in_cop_day = 3450
#     usd_price_in_bs_day = 280000
#     precio_producto_cop = usd_price_in_cop_day * product_price_in_usd
#     precio_producto_bs = usd_price_in_bs_day * product_price_in_usd
#     print (f'USD: {product_price_in_usd}, COP:{precio_producto_cop}, Bs:{precio_producto_bs}')

#     data = {
#       'products':products,
#       'precios_cop':precio_producto_cop,
#       'precios_bs':precio_producto_bs
#     }

#   return render(request, template_name, data)

def conversor(request):
  template_name = 'index.html'
  products = Product.objects.all()

  data = {
    'products':products,
  }
  
  return render(request, template_name, data)