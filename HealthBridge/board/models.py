from django.db import models
from django.utils import timezone
from accounts.models import User
from doctor.models import Doctor

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    answer = models.BooleanField(default=False)
    my_question = models.BooleanField(default=False)
    image = models.ImageField(upload_to="board/", blank=True, null=True)
    hb_user = models.ForeignKey(User, related_name="con_user", on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.pk}]{self.title}"

    def has_answer(self):
        return self.answer


class DoctorAnswer(models.Model):
    answer = models.TextField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="doctor", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[{self.answer}]-{self.doctor}"
