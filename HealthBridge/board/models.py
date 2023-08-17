from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    my_question = models.BooleanField(default=False)
    image = models.ImageField(upload_to="board/", blank=True, null=True)
    hb_user = models.ForeignKey(User, related_name="con_user", on_delete=models.CASCADE)
    # has_answer = models.BooleanField(default=False)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.pk}]{self.title}"

    def has_answer(self):
        return self.answer
