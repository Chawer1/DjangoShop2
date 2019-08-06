from django.db import models
from django.urls import reverse
from django.db.models import Sum

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,)
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    objects = ProductManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    # item_sum =  Product.objects.all().aggregate(Sum("price"))

    def __unicode__(self):
        return "Cart item for product {0}".format(self.product.title)


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __unicode__(self):
        return str(self.id)