# -*- coding: utf-8 -*-
"""
Quick start Serializer
"""
from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Quick start UserSerializer
    """
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Quick start GroupSerializer
    """
    class Meta:
        model = Group
        fields = ('url', 'name')


class PermissionsSerializer(serializers.HyperlinkedModelSerializer):
    """
    Quick start PermissionsSerializer
    """
    class Meta:
        model = Permission
        fields = ('codename', 'name')
