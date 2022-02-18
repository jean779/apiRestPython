from django.shortcuts import render

from programatv.models import ProgramaTV
from programatv.serializers import ProgramaTVSerializer
from rest_framework import viewsets

# Create your views here.
class ProgramaTVViewSet(viewsets.ModelViewSet):
    queryset = ProgramaTV.objects.all().order_by('id')
    serializer_class = ProgramaTVSerializer
