from django.db import models

# Create your models here.
class Coach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharFieldField(max_length= 255)
    