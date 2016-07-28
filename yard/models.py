# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models

from .consts import VEHICLE_TYPE_CHOICES, VEHICLE_TYPE_CAR, \
    VEHICLE_TYPE_MOTORCYCLE
from .managers import CarManager, MotorcycleManager, VehicleManager


class Vehicle(models.Model):
    automaker = models.CharField(max_length=100, db_index=True)
    model = models.CharField(max_length=100, db_index=True)
    color = models.CharField(max_length=30, db_index=True)
    mileage = models.CharField(max_length=15, db_index=True)
    motor_potency = models.CharField(max_length=15, db_index=True)
    type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES)

    objects = VehicleManager()


class Car(Vehicle):

    objects = CarManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.type = VEHICLE_TYPE_CAR
        return super(Car, self).save(*args, **kwargs)


class Motorcycle(Vehicle):

    objects = MotorcycleManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.type = VEHICLE_TYPE_MOTORCYCLE
        return super(Motorcycle, self).save(*args, **kwargs)