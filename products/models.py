from django.db import models

class Product(models.Model):  # Corrected 'model.Model' to 'models.Model'
    image = models.ImageField(upload_to='products/')  # For the product image
    name = models.CharField(max_length=255)  # For the product name
    description = models.TextField()  # For the product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # For the product price
