from django import forms

from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from mainapp.models import ProductCategory


class UserAdminRegisterForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


class UserAdminProductCategory(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __init__(self, *args, **kwargs):
        super(UserAdminProductCategory, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class UserAdminCategoriesForm(UserAdminProductCategory):

    def __init__(self, *args, **kwargs):
        super(UserAdminCategoriesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = False
        self.fields['description'].widget.attrs['readonly'] = False
