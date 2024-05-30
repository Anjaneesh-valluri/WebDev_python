from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    tag = models.TextField(max_length=100,default='000000')
    desc = models.TextField(max_length=100000)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
