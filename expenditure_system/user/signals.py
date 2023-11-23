from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(staff=instance)

       
@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
    instance.profile.save()
