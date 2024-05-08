from django.db import models

class Products(models.Model):
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20),
    description = models.CharField(max_length=100),
    price = models.FloatField()
    create_date = models.DateField(auto_created=True)
    image = models.ImageField(upload_to="shop/products/")