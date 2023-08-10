from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    address = models.TextField()
    telephone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.hospital_name
    
class Doctor(models.Model):
    doctor_user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.PositiveIntegerField(default=0)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_user.username