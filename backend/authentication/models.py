from django.db import models
from django.contrib.auth.models import AbstractUser
from coaches.models import Coach
from clients.models import Client


class User(AbstractUser):
    title = models.ForeignKey(Coach, Client, on_delete= models.CASCADE)
    pass
    '''
    This is a custom version of the built in User class
    It contains all of the built in fields and functionality of the standard User
    You can add fields here for any additional properties you want a User to have
    This is useful for adding roles (Customer and Employee, for example)
    For just a few roles, adding boolean fields is advised
    '''
    # Example (note import of models above that is commented out)
    # this will add a column to the user table
    # is_student = models.BooleanField('student status', default=False)


    #title is going to hold what the user to select either a coach or client
