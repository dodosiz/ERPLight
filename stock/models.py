from django.db import models
from core.models import Department, Product


class Stock(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    initial_date = models.DateField("Initial date")

    class Meta:
        unique_together = ('department', 'product')

    def __str__(self):
        return self.product.name + ': ' + str(self.quantity)
