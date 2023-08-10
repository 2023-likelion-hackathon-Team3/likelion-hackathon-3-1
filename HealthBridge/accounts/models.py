from django.db import models
from django.contrib.auth.models import User
from Post.models import Tag
from board.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


@receiver(post_save, sender=User)
def create_myuser(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_myuser(sender, instance, **kwargs):
    instance.myuser.save()


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to="Files/%Y/%m/%d/")
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.user.username
