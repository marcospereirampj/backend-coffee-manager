# -*- coding: utf-8 -*-

from rest_framework import viewsets
from coffee.models import Member, Registry
from coffee.serializers import MemberSerializer, RegistrySerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class RegistryViewSet(viewsets.ModelViewSet):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer
