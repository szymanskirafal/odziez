from django.db import models

from django.utils.timezone import localdate

import datetime

from orders.models import Order
from employees.models import Employee, Position

class KindOfClothe(models.Model):
    name = models.CharField(max_length = 150, unique = True)
    description = models.CharField(max_length = 300, blank = True)
    time_to_exchange = models.PositiveSmallIntegerField()
    available_for = models.ManyToManyField(Position)

    class Meta:
        verbose_name_plural = 'Rodzaje ubrań'

    def __str__(self):
        return self.name + ' ' + 'wymiana co ' + str(self.time_to_exchange) + 'przysluguje '+ str(self.available_for)

class Clothe(models.Model):
    kind = models.ForeignKey(
        KindOfClothe,
        on_delete = models.CASCADE,
        related_name = 'chosen',)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    employee = models.ForeignKey(
        Employee,
        on_delete = models.CASCADE,
        related_name = 'clothes',
        )
    ordered = models.DateField(null = False, blank = True)
    received = models.DateField(null = True, blank = True)
    owned = models.DateField(null = True, blank = True)
    destroyed = models.DateField(null = True, blank = True)

    class Meta:
        ordering = ['-ordered']
        verbose_name_plural = 'Ubrania pracowników'

    def __str__(self):
        return str(self.name) + ' ' + str(self.employee)


    def can_be_ordered_again(self):
        today = localdate()
        ordered = self.ordered
        days = self.rodzaj.time_to_exchange * 30
        time_to_order_again = datetime.timedelta(days = days)
        if  ordered + time_to_order_again < today:
            return True
        else:
            return False

    def time_to_order_again(self):
        ordered = self.ordered
        days = self.rodzaj.time_to_exchange * 30
        time_to_order_again = datetime.timedelta(days = days)
        date_to_order_again = ordered + time_to_order_again
        return date_to_order_again
