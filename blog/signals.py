from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Author
from account.models import User


@receiver(post_save, sender=User)
def set_nxt_prev_post(sender,instance,*args,created, **kwargs):
    if created:
        if instance.is_staff:
            new_author = Author.objects.create(user=instance)
            new_author.save()

        
        

