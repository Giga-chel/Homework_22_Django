from django.shortcuts import render, get_object_or_404
from .models import Product, Contact


def home(request):
    last_five_products = Product.objects.all().order_by('-created_at')[:5]
    context = {
        'object_list': last_five_products
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    message = None
    contact_info = Contact.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        text = request.POST.get('message')
        print(f"Получено сообщение от {name} ({phone}): {text}")
        message = "Ваше сообщение успешно отправлено!"

    context = {
        'message': message,
        'contact': contact_info
    }
    return render(request, 'catalog/contacts.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_detail.html', context)