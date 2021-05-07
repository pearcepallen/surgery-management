from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    isReceptionist = models.BooleanField(default=False)
    isDoctor = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)



class Staff(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    staffType = models.CharField(max_length=200, null=True, blank=True)
    #surgery = models.ForeignKey('Surgery', on_delete=models.CASCADE, related_name='doctors', null=True, blank=True ) #doctors

    def __str__(self):
        return self.firstName

class Patient(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField()
    contactNumber = models.CharField(max_length=12, null=True, blank=True)


class Room(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    roomName = models.CharField(max_length=200, null=True, blank=True)


class Surgery(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    requestedBy = models.OneToOneField(Staff, on_delete=models.CASCADE, related_name='requested')
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE) #Contemplate making it protected for record purpose
    startDate = models.DateField()
    endDate = models.DateField()
    # doctors = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='surgery', null=True)

    def __str__(self):
        return self.id


class Doctor(models.Model): #Class for multiple doctors per surgery
    id = models.AutoField(primary_key=True, editable=False)
    surgery = models.ForeignKey(Surgery, on_delete=models.CASCADE, related_name='surgery', null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='doctors', null=True)