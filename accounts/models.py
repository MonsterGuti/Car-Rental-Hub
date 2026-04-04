from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.username