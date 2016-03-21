from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TravelSerializer

from .models import Travel

# Create your views here.
class TravelViewSet(viewsets.ModelViewSet):
	queryset = Travel.objects.all()
	serializer_class = TravelSerializer