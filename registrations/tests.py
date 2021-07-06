from django.test import TestCase

from .models import PatientRecord

# Create your tests here.

class TestPatientRecord(TestCase):

    def setUp(self):
        self.patientrecord = PatientRecord.objects.create()


