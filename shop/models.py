from django.db import models

class products(models.Model):
    type = models.CharField(20)
    name = models.CharField(20),
    description = models.CharField(100),
    price = models.FloatField()
    create_date = models.DateField(auto_created=True)
    image = models.ImageField(upload_to="shop/products/")