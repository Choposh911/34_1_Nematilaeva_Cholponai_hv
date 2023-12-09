from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    rate = models.FloatField(default=0)
    img = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')

    def __str__(self):
        return self.title


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
