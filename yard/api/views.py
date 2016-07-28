# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals

from operator import or_
from django.contrib.postgres.search import SearchVector, SearchQuery
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import VehicleSerializer
from ..models import Vehicle


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    # pagination_class = BetterPageNumberPagination

    def list(self, request, *args, **kwargs):
        search_terms = request.GET.get('search', '')
        qs = self.get_queryset()
        if search_terms:
            # apply search
            qs = qs.annotate(search=SearchVector(
                'automaker', 'model', 'color', 'mileage',
                'motor_potency', 'type'
            )).filter(
                search=reduce(or_, map(SearchQuery, search_terms.split(' ')))
            )

        page = self.paginate_queryset(qs)
        serializer = self.get_serializer(page or qs, many=True)
        if page is None:
            return Response(serializer.data)
        else:
            return self.get_paginated_response(serializer.data)
