from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from recipe.models import Product, Warehouse, RawMaterial

def index(request):
    return HttpResponse("Hello, world. You're at the recipe index.")

# Create your views here.
class ProductRecipe(View):
    @staticmethod
    def get(request, *args, **kwargs):
        result = {
            "product_qty": 30
        }

        # get product whose name is "ko'ylak"
        ko_ylak = Product.objects.get(name="ko'ylak")

        result["product_name"] = ko_ylak.name

        product_materials = []
        for recipe in ko_ylak.recipe_set.all():
            pass

