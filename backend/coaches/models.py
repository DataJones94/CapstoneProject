from django.db import models
from authentication.models import User


# Create your models here.
class Coach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length= 255)
    workout = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    

    #I want the coach to be able to have a name, and
    # to be able to access the workouts
