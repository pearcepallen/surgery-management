from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.tokens import RefreshToken
from . models import *


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ['name',]



class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'username', 'email', 'groups']

    def get_id(self, obj):
        return obj.id



class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'username', 'email', 'groups', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)



class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
    


class SurgerySerializer(serializers.ModelSerializer):
    requestedBy = serializers.SerializerMethodField(read_only=True)
    room = serializers.SerializerMethodField(read_only=True)
    patient = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Surgery
        fields = '__all__'

    def get_room(self, obj):
        room = obj.room
        serializer = RoomSerializer(room, many=False)
        return serializer.data

    def get_requestedBy(self, obj):
        requestedBy = obj.requestedBy
        serializer = StaffSerializer(requestedBy, many=False)
        return serializer.data

    def get_patient(self, obj):
        patient = obj.patient
        serializer = PatientSerializer(patient, many=False)
        return serializer.data

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'