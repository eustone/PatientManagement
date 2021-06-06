from django.db import models

# Create your models here.
class PatientRecord(models.Model):
    firstname             = models.CharField(max_length=255)
    lastname              = models.CharField(max_length=255)
    reference_number      = models.CharField(max_length=255)
    patient_id            = models.CharField(max_length=255)
    sickness              = models.CharField(max_length=255, verbose_name="Sickness")
    conditions            = models.TextField()
    additions             = models.TextField()
    date_of_birth         = models.DateField(auto_now=True)
    contact_number        = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True, null=True)
    location              = models.CharField(max_length=255, verbose_name="Facility Name")
    residentialaddress    = models.CharField(max_length=255,verbose_name='Facility Address')
    nationality = models.CharField(max_length=255, verbose_name="Nationality")
    city = models.CharField(max_length=255, verbose_name="City")
    country = models.CharField(max_length=255, verbose_name="Country")
