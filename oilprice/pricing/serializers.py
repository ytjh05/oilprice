from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Position


class PositionSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        field = ['x_position', 'y_position', 'name']

