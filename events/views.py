from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EventSerializer, ParticipantsSerializer
from .models import Event, Participants

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer
