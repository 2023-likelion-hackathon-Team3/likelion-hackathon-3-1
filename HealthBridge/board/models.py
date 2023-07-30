from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    answer = models.TextField(blank=True)
    my_question = models.BooleanField(default=False)
    hb_user = models.ForeignKey(User,related_name='con_user',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title