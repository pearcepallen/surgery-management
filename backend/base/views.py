from django.shortcuts import render
from django.http import HttpResponse
from .decorators import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from django.contrib.auth.models import User
from .models import *
from .serializers import *

# Create your views here.
@allowed_users(allowed_roles=['admin'])
@api_view(['GET'])
def index(request):
    user = request.user

    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

    # return HttpResponse('User type verified')
    