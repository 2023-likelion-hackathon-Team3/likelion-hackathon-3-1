from django.db import models

# Create your models here.

class Quiz(models.Model):
    question = models.TextField(blank=True)
    answer = models.BooleanField()
    explanation = models.TextField(blank=True)

    def __str__(self):
        return self.question

    