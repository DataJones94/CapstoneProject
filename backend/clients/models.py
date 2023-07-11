from django.db import models
from authentication.models import User

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)
    tracker = models.CharField(max_length=255)
    goals = models.CharField(max_length=255)
    name = models.CharField(max_length= 255)
