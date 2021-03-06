from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import *
from base.serializers import *

from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def getSurgeries(request):
    user = request.user
    if request.method == 'POST':
        try:
            if not user.groups.filter(name='receptionist'):
                data = request.data
                requestedBy = Staff.objects.get(id=data['requestedBy'])
                room = Room.objects.get(id=data['room'])
                patient = Patient.objects.get(id=data['patient'])

                docs = data['doctors'].split()

                surgery = Surgery.objects.create(
                    requestedBy = requestedBy,
                    room = room,
                    patient = patient,
                    startDate = data['startDate'],
                    endDate = data['endDate'],
                )
                for doc in docs:
                    surgery.doctors.add(Staff.objects.get(id=doc))
                
                serializer = SurgerySerializer(surgery, many=False)
                return Response({
                    'message':'Successfully created surgery',
                    'code': 0,
                    'data':serializer.data
                    }) 
            else:
                return Response({
                    'message':'Not allowed to create surgery',
                    'code' : 1,
                    })
        except:
            return Response({
            'message':'Patient is already scheduled for surgery | Doctor(s)/Room/Patient does not exist',
            'code': 1,
            })

    doctor = request.GET.get('doctor', '')
    patient = request.GET.get('patient', '')
    room = request.GET.get('room', '')
    
    if doctor and not patient and not room:
        surgeries = Surgery.objects.filter(requestedBy__id=int(doctor))
    elif patient and not doctor and not room:
        surgeries = Surgery.objects.filter(patient__id=int(patient))
    elif room and not doctor and not patient:
        surgeries = Surgery.objects.filter(room__id=int(room))
    elif doctor and patient and not room:
        surgeries = Surgery.objects.filter(requestedBy__id=int(doctor), patient__id=int(patient))
    elif doctor and room and not patient:
        surgeries = Surgery.objects.filter(requestedBy__id=int(doctor), room__id=int(room))
    elif room and patient and not doctor:
        surgeries = Surgery.objects.filter(room__id=int(room), patient__id=int(patient))
    elif doctor and patient and room:
        surgeries = Surgery.objects.filter(requestedBy__id=int(doctor), room__id=int(room), patient__id=int(patient))
    else:
        surgeries = Surgery.objects.all()
    
    serializer = SurgerySerializer(surgeries, many=True)
    return Response({
        'message':'Successfully returned surgeries',
        'code': 0,
        'data':serializer.data
        }) 



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def getSurgery(request, pk):
    try:
        surgery = Surgery.objects.get(id=pk)
        user = request.user

        if request.method == 'PUT':
            if not user.groups.filter(name='receptionist'):
                data = request.data
                surgery.requestedBy = Staff.objects.get(id=data['requestedBy'])
                surgery.room = Room.objects.get(id=data['room'])
                surgery.patient = Patient.objects.get(id=data['patient'])
                surgery.startDate = data['startDate']
                surgery.endDate = data['endDate']

                docs = data['doctors'].split()
                surgery.doctors.clear()

                for doc in docs:
                    surgery.doctors.add(Staff.objects.get(id=doc))
                surgery.save()

                serializer = SurgerySerializer(surgery, many=False)
                return Response({
                    'message':'Successfully updated surgery',
                    'code' : 0,
                    'data' : serializer.data
                    })
            else:
                return Response({
                    'message':'Not allowed to update surgery',
                    'code' : 1,
                    })

        if request.method == 'DELETE':
            if not user.groups.filter(name='receptionist'):
                surgery.delete()
                return Response({
                    'message':'Surgery deleted',
                    'code' : 0
                    })
            else:
                return Response({
                    'message':'Not allowed to delete surgery',
                    'code' : 1,
                    })

        serializer = SurgerySerializer(surgery, many=False)
        return Response({
            'message':'Successfully returned surgery',
            'code' : 0,
            'data' : serializer.data
        }) 

    except:
        return Response({
            'message':'Surgery/Patient/Doctor does not exist | Patient is already scheduled',
            'code' : 1
        })



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSurgeryDoctors(request, pk):
    try:
        surgery = Surgery.objects.get(id=pk)
        doctors = surgery.doctors.all()

        serializer = StaffSerializer(doctors, many=True)
        return Response({
        'message':'Successfully returned doctors',
        'code':0,
        'data':serializer.data
        })

    except:
        return Response({
            'message':'Surgery does not exist',
            'code' : 1
        })