from django.urls import path
from .views import conversor

urlpatterns = [
    path('', conversor, name="conversor"),
]
