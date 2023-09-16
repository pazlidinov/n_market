from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS = (
        ('Sotuvchi', 'Sotuvchi'),
        ('Qabul_qiluvchi', 'Qabul qiluvchi'),
        ('Foydalanuvchi', 'Foydalanuvchi'),
    )
    image = models.ImageField(upload_to='user-images/')
    email = models.EmailField(max_length=200)
    status = models.CharField(max_length=255, choices=STATUS, default='Foydalanuvchi')

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.username}"
    
    def __str__(self):
        return str(self.username)
    