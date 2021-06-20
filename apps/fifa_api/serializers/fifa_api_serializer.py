""" FifaApiSerializer """

# django rest framework 
from rest_framework import serializers

# Models 
from apps.fifa_api.models import Player, Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ['created', 'modified']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ['created', 'modified']