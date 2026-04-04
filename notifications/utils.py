import threading
from .models import Notification


def create_notification(user, message):
    Notification.objects.create(
        user=user,
        message=message
    )


def create_notification_async(user, message):
    thread = threading.Thread(
        target=create_notification,
        args=(user, message)
    )
    thread.start()