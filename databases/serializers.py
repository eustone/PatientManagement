from rest_framework import serializers
from .models import PatientRecord

class PatientRecordSerializer(serializers.Serializer):
    pk           = serializers.IntegerField(read_only=True)
    name         = serializers.CharField(max_length=255)
    reference_number  = serializers.CharField()
    patient_id = serializers.CharField()
    date_of_bith =  serializers.DateTimeField()
    contact_number = serializers.CharField(max_length = 50)
    location       = serializers.CharField(max_length=255)
    address        = serializers.CharField(max_length=255)

    def create(self,validated_data):
        return PatientRecord.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name                 = validated_data.get('name',instance.name)
        instance.reference_number          = validated_data.get('reference_number',instance.reference_number)
        instance.patient_id         = validated_data.get('patient_id'.instance.patient_id)
        instance.date_of_birth         = validated_data.get('date_of_birth',instance.date_of_birth)
        instance.contact_number = validated_data.get('contact_number',instance.contact_number)
        instance.location = validated_data.get('location', instance.location)
        instance.address = validated_data.get('contact_number', instance.address)
        instance.save()
