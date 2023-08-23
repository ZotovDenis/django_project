from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ContactsView, ProductListView, ProductDetailView


app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/products/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/product_detail/', ProductDetailView.as_view(), name='product_detail'),
]
