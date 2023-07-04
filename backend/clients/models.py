from django.db import models

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.IntegerField()
    water = models.IntegerField()
    date = models.DateField()
    name = models.CharFieldField(max_length= 255)
    