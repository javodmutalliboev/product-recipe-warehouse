# product recipe and warehouse api


## Set up database relations
1. Create/change models in models.py
2. Run `py manage.py makemigrations` to create migration files for changes
3. Run `py manage.py migrate` to apply changes to database 

## Create data
1. Run `py manage.py shell` to open the Django shell
2. Run the following commands to create data
```
from recipe.models import Product, Recipe, RawMaterial, Warehouse

#-----------------------------------------------#

# create raw materials
mato =  RawMaterial(name="mato", unit="metr kv")
mato.save()

tugma = RawMaterial(name="tugma", unit="dona")
tugma.save()

ip = RawMaterial(name="ip", unit="metr")
ip.save()

zamok = RawMaterial(name="zamok", unit="dona")
zamok.save()

#-----------------------------------------------#

# create warehouse
mato = RawMaterial.objects.get(name="mato")
tugma = RawMaterial.objects.get(name="tugma")
ip = RawMaterial.objects.get(name="ip")
zamok = RawMaterial.objects.get(name="zamok")

mato1 = Warehouse(raw_material=mato, remaining_quantity=12, price=1500)
mato1.save()

mato2 = Warehouse(raw_material=mato, remaining_quantity=200, price=1600)
mato2.save()

ip1 = Warehouse(raw_material=ip, remaining_quantity=40, price=500)
ip1.save()

ip2 = Warehouse(raw_material=ip, remaining_quantity=300, price=550)
ip2.save()

tugma1 = Warehouse(raw_material=tugma, remaining_quantity=500, price=300)
tugma1.save()

zamok1 = Warehouse(raw_material=zamok, remaining_quantity=1000, price=2000)
zamok1.save()

#-----------------------------------------------#

# create products
product1 = Product(name="ko'ylak", code="k1")
product1.save()

product2 = Product(name="shim", code="s1")
product2.save()

#-----------------------------------------------#

# create recipes
ko_ylak = Product.objects.get(name="ko'ylak")
shim = Product.objects.get(name="shim")

mato = RawMaterial.objects.get(name="mato")
tugma = RawMaterial.objects.get(name="tugma")
ip = RawMaterial.objects.get(name="ip")
zamok = RawMaterial.objects.get(name="zamok")

ko_ylak_recipe = Recipe(product=ko_ylak, raw_material=mato, quantity=0.8)
ko_ylak_recipe.save()

ko_ylak_recipe = Recipe(product=ko_ylak, raw_material=tugma, quantity=5)
ko_ylak_recipe.save()

ko_ylak_recipe = Recipe(product=ko_ylak, raw_material=ip, quantity=10)
ko_ylak_recipe.save()

shim_recipe = Recipe(product=shim, raw_material=mato, quantity=1.4)
shim_recipe.save()

shim_recipe = Recipe(product=shim, raw_material=ip, quantity=15)
shim_recipe.save()

shim_recipe = Recipe(product=shim, raw_material=zamok, quantity=1)
shim_recipe.save()
```