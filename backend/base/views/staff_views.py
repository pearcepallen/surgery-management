from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import *
from base.serializers import *

from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createStaff(request):
    data = request.data
    staff = Staff.objects.create(
        firstName= data['firstName'],
        lastName=data['lastName'],
        email=data['email'],
        phone=data['phone'],
        staffType=data['staffType']
    )

    serializer = StaffSerializer(staff, many=False)
    return Response(serializer.data)   



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def getStaff(request, pk):
    staff = Staff.objects.get(id=pk)

    if request.method == 'PUT':
        data = request.data
        staff.firstName=data['firstName']
        staff.lastName=data['lastName']
        staff.email=data['email']
        staff.phone=data['phone']
        staff.staffType=data['staffType']
        staff.save()

    if request.method == 'DELETE':
        staff.delete()
        return Response('Staff deleted')

    serializer = StaffSerializer(staff, many=False)
    return Response(serializer.data)   