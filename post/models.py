from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    rate = models.FloatField(default=0)
    img = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
