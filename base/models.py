from django.db import models

from django.db import models

class Item(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    itemId = models.IntegerField()
    cat = models.CharField(max_length=255)
    onOffer =models.BooleanField(default=False)
    def __str__(self):
        return self.name
# date = auto_now_add =True
