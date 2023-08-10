from django.shortcuts import render


def home(request):
    """Возвращает главную страницу"""
    return render(request, 'catalog/home.html')


def contacts(request):
    """Возвращает страницу контактов и выводит переданные пользователем данные"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\n'
              f'Телефон: {phone}\n'
              f'Сообщение: {message}')
    return render(request, 'catalog/contacts.html')
