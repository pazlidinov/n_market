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
    product = models.ManyToManyField(
        Product, related_name="delivered_product")
    company_name = models.ForeignKey(
        DeliveringCompany, on_delete=models.CASCADE, related_name='delivering_company', blank=True)
    count = models.FloatField(blank=True, null=True)
    price = models.IntegerField(default=0)
    extra_cost = models.IntegerField(default=0)
    delivered_date = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=150)
<<<<<<< HEAD
    # recipient = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
=======
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
>>>>>>> 7ff981c9de431fb47cca555b16e35d91ae23edaf

    def __str__(self):
        return self.company_name
