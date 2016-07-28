# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers

from .api.views import VehicleViewSet

router = routers.DefaultRouter()
router.register(r'vehicle', VehicleViewSet)

urlpatterns = (
    url(r'^$', TemplateView.as_view(template_name="yard/yard.html"), name='main'),
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),
)
