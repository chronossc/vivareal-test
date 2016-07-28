# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from ..models import Vehicle


class VehicleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vehicle
