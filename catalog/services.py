from django.shortcuts import render

from catalog.forms import ProductForm


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()

    else:
        form = ProductForm()
    return render(request, 'product/create.html', {'form': form})
