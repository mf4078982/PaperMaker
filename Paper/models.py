from django.db import models
# from django.contrib.auth.models import AbstractUser

# class CustomAdmin(AbstractUser):
#     role = models.CharField(
#         max_length= 20,
#         choices=[('Admin','admin'),('Teachers','teachers')],
#         default= 'Teachers'
        
#     )

# Create your models here.
 
class FeedBack(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length= 100)
    message = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.email}"
    
