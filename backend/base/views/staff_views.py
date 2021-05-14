from django.contrib.auth.models import Group

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import *
from base.serializers import *

from django.contrib.auth.hashers import make_password

from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createStaff(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['firstName'],
            last_name=data['lastName'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        userGroup = Group.objects.get(name=data['staffType'])
        userGroup.user_set.add(user)

        staff = Staff.objects.create(
            firstName= data['firstName'],
            lastName=data['lastName'],
            email=data['email'],
            phone=data['phone'],
            staffType=data['staffType'].capitalize()
        )

        user_serializer = UserSerializerWithToken(user, many=False)
        staff_serializer = StaffSerializer(staff, many=False)
        return Response({
            'message':'Successfully created staff member',
            'code' : 0,
            'jwt' : user_serializer.data['token'],
            'user' : staff_serializer.data
        })
    except:
        return Response({
            'message':'User with this email already exists',
            'code' : 1
        })

       



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def getStaff(request, pk):
    try:
        staff = Staff.objects.get(id=pk)

        if request.method == 'PUT':
            data = request.data
            staff.firstName=data['firstName']
            staff.lastName=data['lastName']
            staff.email=data['email']
            staff.phone=data['phone']
            staff.staffType=data['staffType']
            staff.save()

            serializer = StaffSerializer(staff, many=False)
            return Response({
                'message':'Successfully updated staff member',
                'code' : 0,
                'user' : serializer.data
                })

        if request.method == 'DELETE':
            staff.delete()
            return Response({
                'message':'Staff deleted',
                'code' : 0
                })

        serializer = StaffSerializer(staff, many=False)
        return Response({
            'message':'Successfully returned staff member',
            'code' : 0,
            'user' : serializer.data
        })

    except:
        return Response({
            'message':'Staff member does not exist',
            'code' : 1
        })



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDoctors(request):
    doctors = Staff.objects.filter(staffType='Doctor')

    serializer = StaffSerializer(doctors, many=True)
    return Response({
        'message':'Successfully returned doctors',
        'code':0,
        'data':serializer.data
        })   