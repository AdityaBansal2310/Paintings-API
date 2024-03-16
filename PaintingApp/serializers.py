from rest_framework import serializers
from .models import Painting, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id','text', 'created_at' 

class PaintingSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Painting
        fields = '__all__'
