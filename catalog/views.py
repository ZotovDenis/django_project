from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product, Category


# def home(request):
#     """Возвращает главную страницу"""
#     product_list = Category.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Категории'
#     }
#     return render(request, 'catalog/category_list.html', context)

class CategoryListView(ListView):
    model = Category


# def contacts(request):
#     """Возвращает страницу контактов и выводит переданные пользователем данные"""
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Имя: {name}\n'
#               f'Телефон: {phone}\n'
#               f'Сообщение: {message}')
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'catalog/contacts.html', context)

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


# def products(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'products': Product.objects.filter(category=pk),
#         # 'category': category_item.pk,
#         'title': f'{category_item.name}'
#     }
#     return render(request, 'catalog/all_products.html', context)

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
        return context_data


# def product_info(request, pk):
#     context = {
#         'product': Product.objects.get(pk=pk)
#     }
#     return render(request, 'catalog/product_info.html', context)

class ProductDetailView(DetailView):
    model = Product
