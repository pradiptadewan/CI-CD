from django.db import models


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('daily', 'Daily Menu'),
        ('event', 'Event Menu'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='daily')

    def __str__(self):
        return self.name

class Resto(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='resto_images/')

    def __str__(self):
        return self.name
