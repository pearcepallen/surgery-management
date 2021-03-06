from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import *
from base.serializers import *

from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def getPatients(request):
    if request.method == 'POST':
        user = request.user
        if not user.groups.filter(name='doctor'): 
            data = request.data
            patient = Patient.objects.create(
                firstName= data['firstName'],
                lastName=data['lastName'],
                email=data['email'],
                dob=data['dob'],
                contactNumber=data['contactNumber']
            )

            serializer = PatientSerializer(patient, many=False)
            return Response({
                'message':'Successfully created patient',
                'code':0,
                'data':serializer.data
                })
        else:
            return Response({
                    'message':'Not allowed to create patient',
                    'code' : 1,
                    })
    else:
        patients = Patient.objects.all()

        serializer = PatientSerializer(patients, many=True)
        return Response({
            'message':'Successfully returned patients',
            'code':0,
            'data':serializer.data
            })



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def getPatient(request, pk):
    try:
        patient = Patient.objects.get(id=pk)
        user = request.user
        
        if request.method == 'PUT':
            if not user.groups.filter(name='doctor'):
                data = request.data
                patient.firstName=data['firstName']
                patient.lastName=data['lastName']
                patient.email=data['email']
                patient.dob=data['dob']
                patient.contactNumber=data['contactNumber']
                patient.save()

                serializer = PatientSerializer(patient, many=False)
                return Response({
                    'message':'Successfully updated patient',
                    'code' : 0,
                    'user' : serializer.data
                    })
            else:
                return Response({
                    'message':'Not allowed to update patient',
                    'code' : 1,
                    })
        
        if request.method == 'DELETE':
            if not user.groups.filter(name='doctor'):
                patient.delete()
                return Response({
                    'message':'Patient deleted',
                    'code' : 0
                    })
            else:
                return Response({
                    'message':'Not allowed to delete patient',
                    'code' : 1,
                    })

        serializer = PatientSerializer(patient, many=False)
        return Response({
            'message':'Successfully returned patient',
            'code' : 0,
            'data' : serializer.data
            }) 
    except:
        return Response({
            'message':'Patient does not exist',
            'code' : 1
        })
