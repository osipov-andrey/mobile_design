from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib import messages

from django.contrib.auth import logout
# from django.contrib.auth.models import AbstractUser as AdvUser
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin

from .models import AdvUser
from .forms import RegisterUserInfoForm, ChangeUserInfoForm


class RegisterDoneView(TemplateView):
    template_name = 'accounts/register_done.html'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'accounts/register_user.html'
    form_class = RegisterUserInfoForm
    success_url = reverse_lazy('accounts:register_done')


class AccountsPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:profile')
    success_message = 'Пароль пользователя изменен'


class AccountsLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        url = reverse_lazy('main:index')
        return url


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'accounts/delete_user.html'
    success_url = reverse_lazy('main:index')

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, f"Пользователь {request.user.username} удален")
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):

    model = AdvUser
    template_name = 'accounts/change_user_info.html'
    form_class = ChangeUserInfoForm
    # success_url = reverse_lazy('accounts:profile')
    success_url = reverse_lazy('main:index')
    success_message = 'Личные данные пользователя изменены'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


