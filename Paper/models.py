from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomAdmin(AbstractUser):
    role = models.CharField(
        max_length= 20,
        choices=[('Admin','admin'),('Teachers','teachers')],
        default= 'Teachers'
        
    )
