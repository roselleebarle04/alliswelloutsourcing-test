from django.db import models


class OrderType(models.Model):
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description,)


class Order(models.Model):
    order_ref = models.CharField(max_length=30)
    customer_code = models.CharField(max_length=30)
    order_date = models.DateField(null=True, blank=True)
    order_type = models.ForeignKey("OrderType", null=True, blank=True)

    def __str__(self):
        return '%s' % (self.order_ref,)
