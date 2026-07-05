from django.views.generic import ListView, DetailView, CreateView, View
from django.shortcuts import render
from .models import Product, Contact
from .forms import ProductForm


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'page_obj'  # Имя переменной в шаблоне
    paginate_by = 3
    ordering = ['-created_at']


class ContactsView(View):
    def get(self, request):
        contact_info = Contact.objects.first()
        context = {
            'contact': contact_info
        }
        return render(request, 'catalog/contacts.html', context)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        text = request.POST.get('message')
        print(f"Получено сообщение от {name} ({phone}): {text}")

        context = {
            'message': "Ваше сообщение успешно отправлено!",
            'contact': Contact.objects.first()
        }
        return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = '/'  # После создания редирект на главную