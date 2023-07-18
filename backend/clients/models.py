from django.db import models
from authentication.models import User

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User, related_name= 'client_user', on_delete=models.CASCADE)
    coach = models.ForeignKey(User, related_name='coaches',on_delete=models.CASCADE, blank=True, null=True )
    tracker = models.CharField(max_length=255, blank=True, null=True)
    goals = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length= 255)
