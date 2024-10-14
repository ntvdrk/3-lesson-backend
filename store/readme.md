#1
>>> from store.models import Product
>>> all_products = Product.objects.all()
>>> for product in all_products:
>>>    print(product)
... 
Ежик
Посудомойка
Акула

#2
>>> expensive_products = Product.objects.filter(price__gt=100.3) 
>>> for product in expensive_products:
...  print(product)
... 
Ежик
Посудомойка

>>> expensive_products = Product.objects.filter(price__gt=8000)   
>>> for product in expensive_products:
...  print(product)
... 
Ежик

>>> sorted_products = Product.objects.order_by('-price')
>>> for product in sorted_products:
...  print(product)
...
Ежик
Посудомойка
Акула

#3
>>> from store.models import Category 
>>> from store.models import Order    
>>> electronics = Category.objects.create(name="Electronics")
>>> laptop = Product.objects.get(name="Laptop")
>>> laptop.category = electronics
>>> laptop.save()
>>> electronics_products = Product.objects.filter(category=electronics) 
>>> for product in electronics_products:
...  print(product)
... 
Laptop

>>> product_values = Product.objects.values('name', 'price')
>>> for value in product_values:
...  print(value)    
... 
{'name': 'Laptop', 'price': Decimal('5.00')}
{'name': 'Ежик', 'price': Decimal('100000.03')}
{'name': 'Посудомойка', 'price': Decimal('5000.03')}
{'name': 'Акула', 'price': Decimal('100.03')}
>>> product_ids = Product.objects.values_list('id', flat=True)
>>> print(list(product_ids))
[4, 3, 2, 1]

#4
>>> from django.db.models import Q
>>> complex_query = Product.objects.filter(Q(price__gt=100) | Q(product__category=electronics)) 
>>> for product in complex_query:
...  print(product) 
... 
Laptop
>>> complex_exclude = Product.objects.exclude(Q(price__lt=1000) & Q(product__category=electronics))
>>> for product in complex_exclude:
...    print(product)
...
Посудомойка

#5
>>> average_price = Product.objects.aggregate(Avg('price'))
>>> print(f"Average price: {average_price['price__avg']}")
Average price: 26276.2725000000
>>> max_price = Product.objects.aggregate(Max('price')) 
>>> min_price = Product.objects.aggregate(Min('price'))   
>>> print(f"Max price: {max_price['price__max']}, Min price: {min_price['price__min']}")  
Max price: 100000.030000000, Min price: 5

>>> product_order_count = Product.objects.annotate(order_count=Count('price')) 
>>> for product in product_order_count:
...  print(product.name, product.order_count)
... 
Акула 1
Посудомойка 1
Ежик 1
Laptop 1




