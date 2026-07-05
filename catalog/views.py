from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Product, Contact
from .forms import ProductForm


def home(request):
    products_list = Product.objects.all().order_by('-created_at')

    paginator = Paginator(products_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
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


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'catalog/product_form.html', context)
