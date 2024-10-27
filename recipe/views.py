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
        result = []

        # Extract query parameters
        query_params = request.GET

        # Dictionary to track remaining quantities of each warehouse
        warehouse_remaining_qty = {}

        for product_name, product_qty in query_params.items():
            try:
                if product_name == "ko_ylak":
                    product_name = "ko'ylak"

                product = Product.objects.get(name=product_name)
                product_materials = []
                product_qty = int(product_qty)

                for recipe in product.recipe_set.all():
                    raw_material = recipe.raw_material
                    required_qty = recipe.quantity * product_qty
                    warehouses = Warehouse.objects.filter(raw_material=raw_material)

                    for warehouse in warehouses:
                        if warehouse.id not in warehouse_remaining_qty:
                            warehouse_remaining_qty[warehouse.id] = warehouse.remaining_quantity

                        if required_qty <= 0:
                            break

                        if warehouse_remaining_qty[warehouse.id] >= required_qty:
                            qty = required_qty
                            warehouse_remaining_qty[warehouse.id] -= required_qty
                            required_qty = 0
                        elif warehouse_remaining_qty[warehouse.id] > 0:
                            qty = warehouse_remaining_qty[warehouse.id]
                            required_qty -= warehouse_remaining_qty[warehouse.id]
                            warehouse_remaining_qty[warehouse.id] = 0
                        else:
                            continue

                        if raw_material.unit == "dona":
                            qty = int(qty)

                        product_materials.append({
                            "warehouse_id": warehouse.id,
                            "material_name": raw_material.name,
                            "qty": qty,
                            "price": warehouse.price,
                        })

                    if required_qty > 0:
                        qty = required_qty
                        if raw_material.unit == "dona":
                            qty = int(qty)
                        product_materials.append({
                            "warehouse_id": None,
                            "material_name": raw_material.name,
                            "qty": qty,
                            "price": None,
                        })

                result.append({
                    "product_name": product_name,
                    "product_qty": product_qty,
                    "product_materials": product_materials,
                })
            except Product.DoesNotExist:
                continue

        return JsonResponse({"result": result})
