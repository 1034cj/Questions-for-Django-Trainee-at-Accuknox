from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import threading
import logging

# Configure basic logging to display INFO level logs
logging.basicConfig(level=logging.INFO)

# Blog Post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

# Log thread during post creation
current_thread = threading.current_thread().name
logging.info(f"Post creation in thread: {current_thread}")

# Receiver function to handle the post_save signal
@receiver(post_save, sender=Post)
def notify_users(sender, instance, created, **kwargs):
    if created:
        # Log the thread in which the signal is executed
        current_thread = threading.current_thread().name
        logging.info(f"Signal executed in thread: {current_thread}")

        # Send email notification (simplified for demonstration)
        send_mail(
            subject='New Post Created',
            message=f'A new post titled "{instance.title}" has been created.',
            from_email='from@example.com',
            recipient_list=['user@example.com'],
        )
