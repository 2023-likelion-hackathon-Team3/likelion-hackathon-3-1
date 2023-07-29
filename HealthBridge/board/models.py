from django.db import models
from django.utils import timezone

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    answer = models.TextField(blank=True)
    my_question = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title