from django.db import models

from product.models import Product
# from accounts.models import User
# Create your models here.



class DeliveringCompany(models.Model):
    company_name = models.CharField(max_length=150) 
    slug = models.SlugField(max_length=150)
    inn = models.CharField(max_length=150)
    bank = models.CharField(max_length=150)
    code = models.IntegerField(blank=True, null=True)
    mfo = models.IntegerField(blank=True, null=True)
    xisob_raqam = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.company_name

    class Meta:
        # ordering = ["-id"]
        verbose_name_plural = "Delivering Companies"    

class DeliveredItem(models.Model):
    product = models.ManyToManyField(Product, blank=True)
    company_name = models.ForeignKey(
        DeliveringCompany, on_delete=models.CASCADE, related_name='delivering_company', blank=True)
    count = models.FloatField(blank=True, null=True)
    price = models.IntegerField(default=0)
    extra_cost = models.IntegerField(default=0)
    delivered_date = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=150)
    # recipient = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.company_name