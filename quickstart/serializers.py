# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PermissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('codename', 'name')
