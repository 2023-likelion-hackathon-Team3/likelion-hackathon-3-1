from django.db import models

# Create your models here.


class hospital(models.Model):
    name = models.CharField(null=False, max_length=50)
    address = models.TextField(null=False)
    tel = models.TextField(blank=True)

    def __str__(self):
        return self.name
