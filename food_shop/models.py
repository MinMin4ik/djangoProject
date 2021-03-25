from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Category(models.Model):
    # CharField, IntegerField FloatField и другие- это поля модели
    title = models.CharField(max_length=100, verbose_name='Название Категории', help_text='введите название Категория')
    description = models.CharField(max_length=500, verbose_name='Описание')

    # возвращение дефолтного значения при обращении к обьекту

    def __str__(self):
        return self.title

    # Изменение заголовка модели в админке
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Модель блюда со своими полями и методами
class Dish(models.Model):
    # CharField, IntegerField FloatField и другие- это поля модели
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Картинка', max_length=900)
    title = models.CharField(max_length=100, verbose_name='Название блюда', help_text='введите название блюда')
    # связь многие ко многим позволяет связывать множество категорий с множеством товаров
    categories = models.ManyToManyField(Category, verbose_name='категория', )
    company = models.ForeignKey(Company, verbose_name='компания', on_delete=models.SET_NULL, null=True, default=2)
    description = models.CharField(max_length=500, verbose_name='Описание', blank=True)
    # цена не может быть ниже 0, поэтому используется PositiveIntegerField
    price = models.PositiveIntegerField(verbose_name='цена')

    # для корректного отображения категорий
    def get_categories(self):
        return ', '.join([cat.title for cat in self.categories.all()])
    get_categories.short_description = "Категории"

    # возвращение дефолтного значения при обращении к обьекту
    def __str__(self):
        return self.title

    # Изменение заголовка модели в админке
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Cart(models.Model):
    session_key = models.CharField(max_length=999, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_cost = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

    def get_total(self):
        items = CartContent.objects.filter(cart=self.id)
        total = 0
        for item in items:
            total += item.product.price * item.qty
        return total

    def get_cart_content(self):
        return CartContent.objects.filter(cart=self.id)


class CartContent(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Dish, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(null=True)
