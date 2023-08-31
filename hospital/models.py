from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=10)
    # reservation_set = ForeignKey 때문에 생긴 컬럼
    # patient_set = ManyToManyField 때문에 생긴 컬럼


class Patient(models.Model):
    name = models.CharField(max_length=10)
    # reservation_set = 
    doctors = models.ManyToManyField(Doctor, through='Reservation')



class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)