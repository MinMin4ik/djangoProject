
from django.contrib import admin
from .models import Dish, Category, Company, Cart, CartContent, Kit

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Cart)
admin.site.register(CartContent)
admin.site.register(Kit)


# регистрация модели в админке
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    # список отображаемых полей модели
    list_display = ['id', 'title', 'get_categories', 'description']

