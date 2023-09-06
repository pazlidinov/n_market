from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    adress = models.TextField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    manager = models.ForeignKey(User,on_delete=models.PROTECT, related_name="brand_manager")

    def __str__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name




class Producer(models.Model):
    brand_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    inn = models.CharField(max_length=15)

    def __str__(self):
        return str(self.brand_name)

STATUS = (
        ('ready', 'Tayyor'),
        ('being_prepared', 'Tayyorlanmoqda'),
        ('not_available', 'Mavjud emas')
    )
class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    series = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    term = models.DateField(auto_now_add=True)
    entry_price = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    bar_code = models.ImageField(upload_to='product/bar_code/')
    min_count = models.IntegerField(blank=True, null=True)
    commentary = models.TextField(blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=50, blank=True)

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='pr_category')
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.PROTECT, related_name='pr_subcategory')
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='pr_branch')
    measure = models.ForeignKey(
        Measure, on_delete=models.PROTECT, related_name='pr_measure')
    produser = models.ForeignKey(
        Producer, on_delete=models.PROTECT, related_name='pr_producer')

    def __str__(self):
        return str(self.title)


class SaledProduct(models.Model):
    cashier = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user')
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='saled_product')
    count_product = models.ImageField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.time)
