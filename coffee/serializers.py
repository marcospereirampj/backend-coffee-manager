# -*- coding: utf-8 -*-

from rest_framework import serializers
from coffee.models import Member, Registry


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'email')


class RegistrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registry
        fields = ('member', 'date_created')