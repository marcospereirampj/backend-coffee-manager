# -*- coding: utf-8 -*-

from rest_framework import serializers
from coffee.models import Member, Registry


class MemberSerializer(serializers.ModelSerializer):
    registries = serializers.PrimaryKeyRelatedField(many=True, queryset=Registry.objects.all(), required=False)

    class Meta:
        model = Member
        fields = ('name', 'email', 'registries')


class MemberRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return "%s" % (value.name)


class RegistrySerializer(serializers.ModelSerializer):
    member_name = MemberRelatedField(source='member', read_only=True)

    class Meta:
        model = Registry
        fields = ('member', 'date_created', 'member_name')