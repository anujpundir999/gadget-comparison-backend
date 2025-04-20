from django.db import models

class Gadget(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50,default="smartphone")
    specs = models.JSONField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.name}"