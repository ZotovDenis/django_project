from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    """Возвращает главную страницу"""
    product_list = Category.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Категории'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    """Возвращает страницу контактов и выводит переданные пользователем данные"""
    if request.method == 'POST':
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


def products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'products': Product.objects.filter(category=pk),
        'title': f'{category_item.name}'
    }
    return render(request, 'catalog/all_products.html', context)

def product_info(request, pk):
    context = {
        'product': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product_info.html', context)