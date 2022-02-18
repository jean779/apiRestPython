# serializers.py
from rest_framework import serializers

from .models import ProgramaTV

class ProgramaTVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgramaTV
        fields = ('id','nameprogram', 'synopsis', 'agegroup', 'host', 'time', 'broadcaster')
