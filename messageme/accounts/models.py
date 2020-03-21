from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=False)
    Photo = models.ImageField(upload_to='userimage/')

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile.objects.create(user=instance)
#     instance.profile.save()
