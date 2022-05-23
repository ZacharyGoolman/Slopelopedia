from rest_framework import serializers
from .models import Comment 
from .models import Reply
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['user','location', 'latitude', 'longitude', 'post', 'difficulty', 'likes', 'dislikes']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user','video_id','text','likes','dislikes']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id','user','comment_id','comment','text']
        depth = 1
    comment_id = serializers.CharField(write_only=True)