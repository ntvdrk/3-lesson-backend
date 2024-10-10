from django.db import models
from django.contrib.auth.models import User

# 1. Модель Profile с One-to-One связью с User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, verbose_name="Номер телефона", blank=True)
    address = models.CharField(max_length=255, verbose_name="Address", blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return f"Profile of {self.user}"

# 2. Модель Category с выбором типов категорий
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    description = models.TextField(blank=True, verbose_name="Description")
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)
    

# 3. Модель Product с Many-to-One связью с Category
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Product Name")
    description = models.TextField(verbose_name="Product Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to='products/', verbose_name="Product Image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']


    def __str__(self):
        return str(self.name)


# 4. Промежуточная модель OrderItem для связи Many-to-Many между Product и Order
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

# 5. Модель Order с Many-to-Many связью через OrderItem
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {self.pk}"

