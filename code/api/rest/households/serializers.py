from rest_framework import serializers
from .models import EnergyControlling

class EnergyControllingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyControlling
        fields = ('id', 'name', 'ec_type', 'description', 'system_type', 'counter', 'tasks')
