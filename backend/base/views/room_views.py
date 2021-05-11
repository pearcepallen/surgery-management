from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import *
from base.serializers import *

from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def getRooms(request):
    
    if request.method == 'POST':
        data = request.data
        room = Room.objects.create(
            roomName = data['roomName']
        )
        
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data)   
    
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)  


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'PUT':
        data = request.data
        room.roomName=data['roomName']
        room.save()

    if request.method == 'DELETE':
        room.delete()
        return Response('Room deleted')

    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSurgeries(request, pk):
    room = Room.objects.get(id=pk)
    surgeries = room.surgery_set.all()

    serializer = SurgerySerializer(surgeries, many=True)
    return Response(serializer.data)