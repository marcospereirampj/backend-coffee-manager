# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework.views import  APIView
from coffee.models import Member, Registry
from coffee.serializers import MemberSerializer, RegistrySerializer
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import filters


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    ordering_fields = ("name",)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)


class RegistryViewSet(viewsets.ModelViewSet):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer
    ordering_fields = ("member__pk", "member__name", "date_created",)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)


class QueueView(APIView):

    def get(self, request, format=None):
        registries = Registry.objects.all().values('member__name', 'member__pk', 'member__email').\
                annotate(total=Count('member')).order_by('total')
        return Response(registries)




