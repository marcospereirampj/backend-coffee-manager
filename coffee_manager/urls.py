# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from coffee.views_sets import MemberViewSet, RegistryViewSet, QueueView

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'registries', RegistryViewSet)

urlpatterns = [
    url(r'^api/queue/$', QueueView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
