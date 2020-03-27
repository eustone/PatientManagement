from django.db import models

# Create your models here.
class PatientRecord(models.Model):
    name             = models.CharField(max_length=255)
    reference_number = models.CharField(max_length=255)
    patient_id       = models.CharField(max_length=255)
    date_of_birth    = models.DateField(auto_now=True)
    contact_number   = models.CharField(max_length=50)
    location         = models.CharField(max_length=255, verbose_name="Facility Name")
    address          = models.CharField(max_length=255,verbose_name='Facility Address')