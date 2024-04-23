from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
        return self.name


@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if Category.objects.count() == 0:
        Category.objects.create(name='Category 1', description='Description for Category 1')
        Category.objects.create(name='Category 2', description='Description for Category 2')

    if Product.objects.count() == 0:
        category1 = Category.objects.get(name='Category 1')
        Product.objects.create(name='Product 1', description='Description for Product 1', price=10.99,
                               category=category1)
        Product.objects.create(name='Product 2', description='Description for Product 2', price=19.99,
                               category=category1)