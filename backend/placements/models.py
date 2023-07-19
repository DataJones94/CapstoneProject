from django.db import models

class Placement(models.Model):
    coach = models.CharField(max_length=255)
    client = models.CharField(max_length=255)






    
# Create your models here. this is to take place of the User