from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from .forms import UserRegisterForm, UserLoginForm, UserProfileForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            subject='Добро пожаловать в Skystore!',
            message=f'Здравствуйте, {self.object.email}!\n\nСпасибо за регистрацию в нашем магазине.',
            from_email='admin@skystore.com',
            recipient_list=[self.object.email],
            fail_silently=False,
        )
        return response

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = None
    form_class = UserProfileForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('users:profile_edit')

    def get_object(self, queryset=None):
        return self.request.user
