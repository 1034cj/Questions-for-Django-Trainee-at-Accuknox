from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def update_status_on_save(sender, instance, **kwargs):
    print("Signal handler called")
    # Change the status and save
    instance.status = 'Processed by signal'
    instance.save()
