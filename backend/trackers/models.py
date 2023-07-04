from django.db import models
from authentication.models import User

# Create your models here.
class Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.IntegerField()
    water = models.IntegerField()
    