from django.db import models
from authentication.models import User
from placements import Placement


# Create your models here.
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upper_body = models.CharField(max_length= 255)
    upper_body_date = models.DateField(null=True)
    lower_body = models.CharField(max_length=255)
    lower_body_date = models.DateField(null=True)
    cardio = models.CharField(max_length=255)
    cardio_date = models.DateField(null=True)


    #User will be able to have an upper and lower body workout and 
    #a cardio workout. And the user will have different dates scheduled to workout
    # example: mondays are upper body, wednesdays are lower body, fridays are cardio



