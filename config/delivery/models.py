# from django.db import models
# from product.models import Product
# from django.contrib.auth.models import User

# # Create your models here.




# class DeliveredItem(models.Model):
#     company_name = models.ForeignKey(
#         DeliverCompany, on_delete=models.CASCADE, related_name='delivering_company')
#     name = models.CharField(max_length=150)
#     slug = models.SlugField(max_length=150)
#     delivery_name = models.CharField(max_length=150)
#     weight = models.FloatField(blank=True, null=True)
#     delivered_date = models.DateField(auto_now_add=True)
#     region = models.CharField(max_length=150)
#     product = models.ManyToManyField(Product, blank=True)

#     def __str__(self):
#         return self.name


# class DeliverCompany(models.Model):
#     company_name = models.CharField(max_length=150)
#     slug = models.SlugField(max_length=150)
#     inn = models.CharField(max_length=150)
#     bank = models.CharField(max_length=150)
#     code = models.IntegerField(blank=True, null=True)
#     mfo = models.IntegerField(blank=True, null=True)
#     xisob_raqam = models.IntegerField(blank=True, null=True)
    
#     def __str__(self):
#         return self.company_name