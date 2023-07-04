from django.db import models

# Create your models here.
class Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.IntegerField()
    water = models.IntegerField()
    