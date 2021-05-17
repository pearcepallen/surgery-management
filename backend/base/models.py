from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=200, null=True, blank=True)
    staffType = models.CharField(max_length=200, null=True, blank=True)
    authCode = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.id} | {self.firstName} | {self.lastName} | {self.staffType}'

class Patient(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField()
    contactNumber = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return f'{self.id} | {self.firstName} | {self.lastName} | {self.dob}'


class Room(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    roomName = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.id} | {self.roomName}'


class Surgery(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    requestedBy = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='requested')
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE) 
    startDate = models.DateField()
    endDate = models.DateField()
    doctors = models.ManyToManyField(Staff, blank=True)

    def __str__(self):
        return f'{self.id} __ {self.requestedBy} __ {self.room} __ {self.patient}'
