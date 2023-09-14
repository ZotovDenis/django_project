
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache

from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version

from config.settings import CACHE_ENABLED


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if CACHE_ENABLED:
            key = 'categories_list'
            categories_list = cache.get(key)
            if categories_list is None:
                categories_list = self.model.objects.all()
                cache.set(key, categories_list)
        else:
            categories_list = self.model.objects.all()

        context_data['categories'] = categories_list
        return context_data



class ContactsView(View):
    def get(self, request):
        context = {
            'title': 'Контакты'
        }
        return render(request, 'catalog/contacts.html', context)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\n'
              f'Телефон: {phone}\n'
              f'Сообщение: {message}')
        context = {
            'title': 'Контакты'
        }
        return render(request, 'catalog/contacts.html', context)


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        category_item = Category.objects.get(pk=self.kwargs['pk'])
        context_data['title'] = category_item.name

        for product in context_data['products']:
            version = product.version_set.first()
            product.version = version
        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product = context_data['product']

        active_versions = Version.objects.filter(product=product, is_active=True)

        context_data['active_versions'] = active_versions
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return self.handle_no_permission()
        form.instance.user = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        return render(self.request, 'catalog/create_product_error.html')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return render(self.request, 'catalog/create_version_error.html')
        return super().dispatch(request, *args, **kwargs)


def product_list(request):
    products = Product.objects.all()
    versions = Version.objects.filter(is_active=True)

    context = {
        'продукты': products,
        'версии': versions
    }

    return render(request, 'product_list.html', context)


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.cleaned_data.get('product')

        if product.user != self.request.user:
            return render(self.request, 'catalog/create_version_error.html')

        return super().form_valid(form)
