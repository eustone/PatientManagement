from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics

from . import models
from . import serializers

# Create your views here.


class ListCreatePatientRecord(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = models.PatientRecord.objects.all()
    serializer_class = serializers. PatientRecordSerializer
    template_name = 'index.html'


class ListPatientRecordView(generics.ListAPIView):
    pass