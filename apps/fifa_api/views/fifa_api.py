""" FifaApi ViewSet """
# Django
from django.utils import timezone


# django rest framework 
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import AllowAny
from ..permissions import IsAuthToken

# Models
from apps.fifa_api.models import Player, Team, IntegrationServices

# Serializers
from ..serializers import PlayerSerializer, TeamSerializer

# Utils - Services 
from core.utils.services import FifaServices

class TeamViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    fifa_services = FifaServices()


    def get_permissions(self):
        if self.action in ['team']:
            permissions = [IsAuthToken]
        else: 
            permissions = [AllowAny]
        
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def team(self, request, *args, **kwargs):
        data_request = request.data
        
        data = {
            "count": count,
            "players": data_fifa
        }
        return Response(data)
    
    def load_data(self):
        integrations_services = IntegrationServices.objects.filter(already_integrated=True).count()
        if integrations_services < 1:
            time_start = timezone.datetime.now()
            self.fifa_services.save_data()
            time_finish = timezone.datetime.now()

            IntegrationServices.objects.create(
              already_integrated = True,
              start_integration = time_start,
              finish_integration = time_finish
            )
        
        else:
            return False, 0, 0