from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from rest_framework import generics

from . import models
from . import serializers

# Create your views here.

class PatientListView(ListView):
    model = models.PatientRecord
    template_name = 'all_patients_records.html'


class PatientDetailView(DetailView):
    model = models.PatientRecord
    template_name = 'patient_detail_record.html'

class PatientDeleteView(DeleteView):
    model = models.PatientRecord
    template_name = 'delete_patient_record.html'

class PatientUpdateView(UpdateView):
    model = models.PatientRecord
    template_name = 'update_patient_record.html'



class ListCreatePatientRecord(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = models.PatientRecord.objects.all()
    serializer_class = serializers. PatientRecordSerializer
    template_name = 'index.html'


class ListPatientRecordView(generics.ListAPIView):
    pass