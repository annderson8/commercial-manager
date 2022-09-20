from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=40)
    type_product = models.CharField(max_length=30)