
from django.urls import path
from food_shop import views
from django.conf import settings
from django.contrib.auth import logout

urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('category/', views.view_category, name="category"),
    path('cart/', views.CartView.as_view(), name='cart'),
    # user actions
    path('edit/', views.edit_profile, name="edit"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name='log_out'),
    path('register/', views.register, name="register"),

]