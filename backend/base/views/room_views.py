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
    user = request.user

    if request.method == 'POST':
        if user.groups.filter(name='admin'):
            data = request.data
            room = Room.objects.create(
                roomName = data['roomName']
            )
            
            serializer = RoomSerializer(room, many=False)
            return Response({
                    'message':'Successfully created room',
                    'code': 0,
                    'data':serializer.data
                    })   
        else:
            return Response({
                    'message':'Not allowed to create a room',
                    'code' : 1,
                    })
    
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response({
        'message':'Successfully returned rooms',
        'code': 0,
        'data':serializer.data
        })  


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def getRoom(request, pk):
    try:
        user = request.user
        room = Room.objects.get(id=pk)

        if request.method == 'PUT':
            if user.groups.filter(name='admin'):
                data = request.data
                room.roomName=data['roomName']
                room.save()

                serializer = RoomSerializer(room, many=False)
                return Response({
                    'message':'Successfully updated room',
                    'code' : 0,
                    'data' : serializer.data
                    })
            else:
                return Response({
                        'message':'Not allowed to update a room',
                        'code' : 1,
                        })

        if request.method == 'DELETE':
            if user.groups.filter(name='admin'):
                room.delete()
                return Response({
                        'message':'Room deleted',
                        'code' : 0
                        })
            else:
                return Response({
                        'message':'Not allowed to delete a room',
                        'code' : 1,
                        })

        serializer = RoomSerializer(room, many=False)
        return Response({
                'message':'Successfully returned room',
                'code' : 0,
                'data' : serializer.data
            })

    except:
        return Response({
            'message':'Room does not exist',
            'code' : 1
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSurgeries(request, pk):
    try:
        room = Room.objects.get(id=pk)
        surgeries = room.surgery_set.all()

        serializer = SurgerySerializer(surgeries, many=True)
        return Response({
            'message': 'Successfully returned surgeries',
            'code': 0,
            'data':serializer.data
            })

    except:
        return Response({
            'message':'Room does not exist',
            'code' : 1
        })