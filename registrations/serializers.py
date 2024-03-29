from rest_framework import serializers
from .models import PatientRecord

class PatientRecordSerializer(serializers.Serializer):

    """The Patient Record Serializer object """
    
    pk           = serializers.IntegerField(read_only=True)
    patient_id = serializers.CharField()
    patient_reference_number  = serializers.CharField() 
    title = serializers.CharField(max_length=10)
    firstname         = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)  
    gender         = serializers.CharField(max_length=10)  
    sickness = serializers.CharField(max_length=255)   
    conditions = serializers.CharField(max_length=255)
    notes = serializers.CharField(max_length=255)
    date_of_birth =  serializers.DateTimeField()
    contact_number = serializers.CharField(max_length = 50)
    email = serializers.EmailField(max_length=255)
    location = serializers.CharField(max_length=255)
    residentialaddress = serializers.CharField(max_length=255)
    nationality = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=255)

    def create(self,validated_data):
        return PatientRecord.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.patient_id         = validated_data.get('patient_id'.instance.patient_id)
        instance.patient_reference_number = validated_data.get('reference_number',instance.reference_number)
        instance.title = validated_data.get('title', instance.title)
        instance.firstname          = validated_data.get('firstname',instance.name)
        instance.lastname           = validated_data.get('lastname',instance.name)           
        instance.gender = validated_data.get('gender', instance.gender)
        instance.conditions         = validated_data.get('conditions', instance.conditions)
        instance.sickness           = validated_data.get('sickness', instance.sickness)
        instance.notes              = validated_data.get('notes', instance.notes)
        instance.date_of_birth      = validated_data.get('date_of_birth',instance.date_of_birth)
        instance.contact_number = validated_data.get('contact_number',instance.contact_number)
        instance.email = validated_data.get('email', instance.email)
        instance.location = validated_data.get('location', instance.location)
        instance.residentialaddress = validated_data.get('residential address', instance.address)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
