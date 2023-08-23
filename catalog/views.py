from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product, Category


class CategoryListView(ListView):
    model = Category


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
        return context_data


class ProductDetailView(DetailView):
    model = Product
