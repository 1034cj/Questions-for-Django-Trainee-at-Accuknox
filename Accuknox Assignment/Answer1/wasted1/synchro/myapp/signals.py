import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulate a delay to show synchronous blocking
    print("Signal handler finished.")

# Code to trigger the signal
print("Creating a user instance...")
user = User.objects.create(username="testuser")
print("User instance created.")