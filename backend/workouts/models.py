from django.db import models
from authentication.models import User


# Create your models here.
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.CharField(max_length= 255)
