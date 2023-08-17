from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products, product_info


app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products/', products, name='products'),
    path('<int:pk>/product_info/', product_info, name='product_info'),
]
