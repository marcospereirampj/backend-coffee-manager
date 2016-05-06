# -*- coding: utf-8 -*-

from rest_framework import serializers
from coffee.models import Member, Registry


class MemberSerializer(serializers.ModelSerializer):
    '''
        Modelo de usuários
    '''
    registries = serializers.PrimaryKeyRelatedField(many=True, queryset=Registry.objects.all(), required=False)

    class Meta:
        model = Member
        fields = ('name', 'email', 'registries')

class RegistrySerializer(serializers.ModelSerializer):
    member_name = serializers.SerializerMethodField(source="get_member_name")

    def get_member_name(self, obj):
        return obj.member.name

    class Meta:
        model = Registry
        fields = ('member', 'date_created', 'member_name')
