from django.db import models
from authentication.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name= 'post_user', on_delete=models.CASCADE)
    client = models.ForeignKey(User, related_name='post_client',on_delete=models.CASCADE, blank=True, null=True )

