import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('ball', 'Ball'),
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('accessory', 'Accessory'),
        ('equipment', 'Equipment'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    description = models.TextField(default="")
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='accessory')
    product_views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
        
    def increment_views(self):
        self.product_views += 1
        self.save()