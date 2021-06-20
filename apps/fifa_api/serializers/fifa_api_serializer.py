""" FifaApiSerializer """

# django rest framework 
from apps.fifa_api.models.integration_services import IntegrationServices
from rest_framework import serializers

# Models 
from apps.fifa_api.models import Player, Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ['created', 'modified']


class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Player
        exclude = ['created', 'modified', 'page_saved']


class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationServices
        exclude = ['created', 'modified']