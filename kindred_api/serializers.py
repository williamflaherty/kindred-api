from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from kindred_api import models

class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return model.User(**validated_data)
    
    class Meta:
        model = models.User
        fields = ('id', 'username', 'ig_token', 'ig_token_expiry', 'join_date')

class ChallengeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Challenge
        fields = ('id', 'challenge', 'pub_date', 'completions') 

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Photo
        fields = ( 'id', 'url', 'challenge', 'user', 'pub_date', 'updoots', 'downvotes', 'instagram', 'flagged', 'city', 'top_tf' )
