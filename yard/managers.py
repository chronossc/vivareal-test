# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models

from .consts import VEHICLE_TYPE_CAR, VEHICLE_TYPE_MOTORCYCLE


class VehicleManager(models.Manager):

    def cars(self):
        return self.filter(type=VEHICLE_TYPE_CAR)

    def motorcycles(self):
        return self.filter(type=VEHICLE_TYPE_MOTORCYCLE)


class CarManager(VehicleManager):

    def get_queryset(self):
        return super(CarManager, self).get_queryset().filter(type=VEHICLE_TYPE_CAR)


class MotorcycleManager(VehicleManager):

    def get_queryset(self):
        return super(MotorcycleManager, self).get_queryset().filter(type=VEHICLE_TYPE_MOTORCYCLE)
