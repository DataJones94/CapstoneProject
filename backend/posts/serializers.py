from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user_id', 'client_id', 'coach_id', 'tips', 'encouragement']
        depth = 1