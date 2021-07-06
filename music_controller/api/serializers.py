from django.db.models import fields
from rest_framework import serializers
from .models import Games, Room, Article


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')


class UpdateRoomSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])

    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')


class ArticleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class GameSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'