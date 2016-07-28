# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext as _

VEHICLE_TYPE_CAR = 'car'
VEHICLE_TYPE_MOTORCYCLE = 'motorcycle'

VEHICLE_TYPE_CHOICES = (
    (VEHICLE_TYPE_CAR, _('Car')),
    (VEHICLE_TYPE_MOTORCYCLE, _('Motorcycle'))
)
