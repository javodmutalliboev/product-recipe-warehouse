from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('product-recipe/', views.ProductRecipe.as_view(), name="product-recipe"),
]