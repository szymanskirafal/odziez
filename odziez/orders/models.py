from django.db import models

from employees.models import Manager, WorkPlace

class Order(models.Model):
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE)
    place_of_delivery = models.ForeignKey(WorkPlace, on_delete = models.CASCADE)
    during_composing = models.BooleanField(default = True)
    composed = models.BooleanField(default = False)
    sent_to_supervisor = models.BooleanField(default = False)
    date_of_sending_to_supervisor = models.DateField(null = True, blank = True)
    approved_by_supervisor = models.BooleanField(default = False)
    sent_to_manufacturer = models.BooleanField(default = False)
    date_of_sending_to_manufacturer = models.DateField(null = True, blank = True)
    received_from_manufacturer = models.BooleanField(default = False)
    date_of_receiving_from_manufacturer = models.DateField(null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Zamówienia'
