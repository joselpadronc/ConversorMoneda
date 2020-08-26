from django.shortcuts import render
from django.http import HttpResponse

# Models
from .models import Product

# Create your views here.


def home_page(request):
  products = Product.objects.all()

  data = {
    'products':products
  }

  return render(request, 'index.html', data)



def conversor_usd_cop(request):
  template_name = 'price_usd_cop.html'
  products_prices = Product.objects.all()

  for product_price in products_prices:
    product_price_in_usd = product_price.product_price_usd

    usd_price_in_cop_day = 3450
    precio_producto_cop = usd_price_in_cop_day * product_price_in_usd
    print(f'USD: {product_price_in_usd}, COP {precio_producto_cop}')

  
  return render(request, template_name)


def conversor_usd_bs(request):
  template_name = 'price_usd_bs.html'
  precio_productos = Product.objects.all()

  for precio_producto in precio_productos:
    precio_producto_usd = precio_producto.product_price_usd
    
    precio_usd_bs_dia = 248209
    precio_producto_bs = precio_usd_bs_dia * precio_producto_usd
    print(f'USD: {precio_producto_usd}, Bs {precio_producto_bs}')
  
  return render(request, template_name)