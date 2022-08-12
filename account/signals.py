from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User


# @receiver(post_save, sender=User)
# def user_info_handler(sender,created,instance,*args, **kwargs):
#     if instance or created:
#         q = UserProfile.objects.filter(user=instance)
#         if not q.exists():
#             UserProfile.objects.create(user=instance,name=instance.username) 


   