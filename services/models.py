from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes", null=True, blank=True)
    image = models.ImageField(upload_to='services/', blank=True, default="default.jpg")
    special_offer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name