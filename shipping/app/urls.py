from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.ShipmentView.as_view(), name='shipment_view')
]