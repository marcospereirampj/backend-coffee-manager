# -*- coding: utf-8 -*-

from rest_framework import serializers
from coffee.models import Member, Registry


class MemberSerializer(serializers.ModelSerializer):
    registries = serializers.PrimaryKeyRelatedField(many=True, queryset=Registry.objects.all())

    class Meta:
        model = Member
        fields = ('name', 'email', 'registries')


class RegistrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Registry
        fields = ('member', 'date_created')
        depth = 2