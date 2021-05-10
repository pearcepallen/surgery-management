from django.shortcuts import render
from django.http import HttpResponse
from .decorators import *

# Create your views here.

@allowed_users(allowed_roles=['admin'])
def index(request):
    return HttpResponse('User type verified')
    