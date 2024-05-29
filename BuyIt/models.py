from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=100)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class cart(models.Model):
    
