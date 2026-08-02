from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from .models import Product, Contact
from .forms import ProductForm

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'page_obj'
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        obj = self.get_object()
        is_owner = obj.owner == self.request.user
        is_moderator = self.request.user.has_perm('catalog.delete_product')
        return is_owner or is_moderator

class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.is_published = False
        product.save()
        return redirect('catalog:product_detail', pk=pk)
