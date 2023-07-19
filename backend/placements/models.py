from django.db import models

class Placement(models.Model):
    coach = models.CharField(max_length=255)
    client = models.CharField(max_length=255)







# Create your models here. 
# created placement app to take place of the User 
# going to put a slot into the coach and clent class 
# of what eachone was anf figured itd be easier 
# to put it in authentaction model so when they
#  register for a user they know what title to pick