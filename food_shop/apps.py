from django.apps import AppConfig


class ShopConfig(AppConfig):
    name = 'food_shop'

    def ready(self):
        import food_shop.signals