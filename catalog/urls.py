from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ContactsView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/products/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/product_detail/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('createversion/', VersionCreateView.as_view(), name='create_version')
]
