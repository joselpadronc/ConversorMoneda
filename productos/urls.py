from django.urls import path
from .views import home_page, conversor_usd_cop, conversor_usd_bs

urlpatterns = [
    path('', home_page, name="home_page"),
    path('usd-cop/', conversor_usd_cop, name="usd_cop_page"),
    path('usd-bs/', conversor_usd_bs, name="usd_bs_page"),
]
