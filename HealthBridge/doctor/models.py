from django.db import models
from django.contrib.auth.models import User
from board.models import Board
from django.utils import timezone


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    address = models.TextField()
    telephone = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return self.hospital_name


class Doctor(models.Model):
    doctor_user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="doctor_user"
    )
    license_number = models.PositiveIntegerField(default=0)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    history = models.TextField(null=True, blank=True)
    introduction = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.doctor_user.username


class DoctorAnswer(models.Model):
    answer = models.CharField(max_length=300)
    board_list = models.ForeignKey(Board, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="doctor", on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.answer}]-{self.doctor}"
