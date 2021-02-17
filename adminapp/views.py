from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from authapp.models import User
from mainapp.models import ProductCategory
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, UserAdminProductCategory, \
    UserAdminCategoriesForm


@user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('index'))
def index(request):
    return render(request, 'adminapp/index.html')


# CBV

# Users
class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование пользователя'
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Categories
class ProductCategoriesView(ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductCategoriesCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-category-create.html'
    success_url = reverse_lazy('adminapp:admin_products_categories')
    form_class = UserAdminProductCategory


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-categories-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_products_categories')

    form_class = UserAdminCategoriesForm

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView,
                        self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование категории'
        return context


class ProductCategoryDelete(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-categories-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_products_categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
