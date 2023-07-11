from django.db import models
from authentication.models import User
# Create your models here.

class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sqauts = models.IntegerField()
    lunges = models.IntegerField()
    dead_lifts = models.IntegerField()
    shoulder_press = models.IntegerField()
    bicep_curls = models.IntegerField()
    tricep_kickbacks = models.IntegerField()
