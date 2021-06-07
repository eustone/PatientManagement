from django.db import models

# Create your models here.
class PatientRecord(models.Model):
    """The Patient Record containing all
     important information about an individual"""
    # Title Choices
    title_choices = (
        ('mr' , 'Mr'  ), ('mrs' , 'Mrs'),
        ('miss','Miss'), ('ms', 'Ms'),
        ('doctor', 'Doctor'),('professor', 'Professor'),)

    patient_id            = models.CharField(max_length=255)
    patient_reference_number = models.CharField(max_length=255)
    title = models.CharField(max_length=10, choices= title_choices)
    firstname             = models.CharField(max_length=255)
    lastname              = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')))
    sickness              = models.CharField(max_length=255, verbose_name="Sickness")
    conditions            = models.TextField()
    notes                 = models.TextField()
    date_of_birth         = models.DateTimeField(auto_now=True)
    contact_number        = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True, null=True)
    location              = models.CharField(max_length=255, verbose_name="Facility Name")
    residentialaddress    = models.CharField(max_length=255,verbose_name='Residential Address')
    nationality = models.CharField(max_length=255, verbose_name="Nationality")
    city = models.CharField(max_length=255, verbose_name="City")
    country = models.CharField(max_length=255, verbose_name="Country")
