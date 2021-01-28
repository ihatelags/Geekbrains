from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название категории')
    description = models.TextField(blank=True, null=True, verbose_name='Описание категории')
    url = models.TextField(blank=True, null=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to='products_images', blank=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    short_description = models.CharField(max_length=64, blank=True, verbose_name='Короткое описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    url = models.TextField(blank=True, null=True, verbose_name='Ссылка')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category.name}'
