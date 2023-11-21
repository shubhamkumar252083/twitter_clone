# code
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from user.models import User


@receiver(pre_save, sender=User)
def user_model_pre_save_action(sender, instance, **kwargs):
    # Modify or validate data just before saving
    # instance.name = instance.name.upper()  # Convert name to uppercase before saving
    print(f'user_model_pre_save_action.email ==> {instance.email}')


@receiver(post_save, sender=User)
def user_model_post_save_action(sender, instance, **kwargs):
    # Your custom logic here
    print(f'user_model_pre_save_action.mobile ==> {instance.mobile}')