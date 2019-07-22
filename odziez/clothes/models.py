from django.db import models

from django.utils.timezone import localdate

import datetime

from orders.models import Order
from employees.models import Employee, Position


class Manufacturer(models.Model):
    name = models.CharField(max_length = 150, unique = True)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Producenci'

    def __str__(self):
        return self.name


class KindOfClothe(models.Model):
    name = models.CharField(max_length = 150, unique = True)
    description = models.CharField(max_length = 300, blank = True)
    months_to_exchange = models.PositiveSmallIntegerField()
    available_for = models.ManyToManyField(Position)
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Rodzaje ubrań'

    def __str__(self):
        return self.name + ' ' + 'wymiana co ' + str(self.months_to_exchange) + 'przysluguje '+ str(self.available_for)


class Clothe(models.Model):
    kind = models.ForeignKey(
        KindOfClothe,
        on_delete = models.CASCADE,
        related_name = 'chosen',
        )
    order = models.ForeignKey(
        Order,
        on_delete = models.CASCADE,
        related_name = 'clothes_ordered',
        )
    employee = models.ForeignKey(
        Employee,
        on_delete = models.CASCADE,
        related_name = 'clothes',
        )
    prepared_to_order = models.BooleanField(null = False, blank = False, default = False)
    ordered = models.DateField(null = True, blank = True)
    received = models.DateField(null = True, blank = True)
    owned = models.DateField(null = True, blank = True)
    destroyed = models.DateField(null = True, blank = True)

    class Meta:
        ordering = ['-ordered']
        verbose_name_plural = 'Ubrania pracowników'

    def __str__(self):
        return str(self.kind) + ' ' + str(self.employee)


    def can_be_ordered_again(self):
        today = localdate()
        if self.ordered == None:
            return True
        else:
            ordered = self.ordered
            days = self.kind.months_to_exchange * 30
            time_to_order_again = datetime.timedelta(days = days)
            if  ordered + time_to_order_again < today:
                return True
            else:
                return False

    def time_to_order_again(self):
        ordered = self.ordered
        days = self.kind.months_to_exchange * 30
        time_to_order_again = datetime.timedelta(days = days)
        date_to_order_again = ordered + time_to_order_again
        return date_to_order_again
