from django.db import models

from authapp.models import User
from mainapp.models import Product


class BasketQuerySet(models.QuerySet):

    def delete(self):
        for obj in self:
            obj.product.quantity += obj.quantity
            obj.product.save()
        super().delete()


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_basket(self):
        return Basket.objects.filter(user=self.user)

    def total_sum(self):
        return sum([basket.sum() for basket in self.total_basket()])

    def total_qty(self):
        return sum([basket.quantity for basket in self.total_basket()])

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category')

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete()

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)
