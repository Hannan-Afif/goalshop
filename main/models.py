import uuid
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('ball', 'Football'),
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('accessory', 'Accessory'),
        ('equipment', 'Equipment'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField(default="")
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='accessory')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name