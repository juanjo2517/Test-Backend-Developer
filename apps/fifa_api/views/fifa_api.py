""" FifaApi ViewSet """
# Django
from django.utils import timezone
from django.db.models import Q

# django rest framework 
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

# Permissions
from rest_framework.permissions import AllowAny
from ..permissions import IsAuthToken

# Models
from apps.fifa_api.models import Player, Team, IntegrationServices

# Serializers
from ..serializers import PlayerSerializer, IntegrationSerializer

# Utils - Services 
from core.utils.services import FifaServices

# Filters
from django_filters import rest_framework as filters
import django_filters

class PlayersFilter(filters.FilterSet):
    order = django_filters.CharFilter(method="get_order")
    page = django_filters.NumberFilter(field_name='page_saved', lookup_expr='exact')

    class Meta:
        model = Player
        fields = ['order', 'page']
    
    def get_order(self, queryset, name, value):
        if value == "desc":
            return Player.objects.all().order_by('-first_name')
        else:
            return Player.objects.all().order_by('first_name')

class PlayerViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    fifa_services = FifaServices()

    search_fields = [
        'first_name',
        'last_name'
    ]
    
    filter_backends = [SearchFilter, filters.DjangoFilterBackend]
    filterset_class = PlayersFilter

    def get_permissions(self):
        if self.action in ['team', 'players', 'load']:
            permissions = [IsAuthToken]
        else: 
            permissions = [AllowAny]
        
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def team(self, request):
        page = request.data.get('page', None)
        name_team = request.data.get('name', None)

        if not page:
            return Response({"page": "Campo Obligatorio"}, status=status.HTTP_400_BAD_REQUEST)
        if not name_team:
            return Response({"name": "Campo Obligatorio"}, status=status.HTTP_400_BAD_REQUEST)


        is_team = True
        queryset = self.filter_queryset(self.get_queryset(page, name_team, is_team))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def players(self, request):
        is_team = False
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    def get_queryset(self, page = None, name_team = None, is_team = False):
        if is_team and page is not None:
            query =  Player.objects.filter(
                Q(team__name__icontains=name_team),
                page_saved = page
            ).distinct()
        else:
            query = Player.objects.all()
        return query
    


    @action(detail=False, methods=['get'])
    def load(self, request):
        integrations_services = IntegrationServices.objects.filter(already_integrated=True).count()
        if integrations_services < 1:
            time_start = timezone.datetime.now()
            is_integrate, teams, players = self.fifa_services.save_data()
            time_finish = timezone.datetime.now()

            integrate = IntegrationServices.objects.create(
              already_integrated = True,
              start_integration = time_start,
              finish_integration = time_finish,
              num_teams = teams,
              num_players = players,
            )

            data = {
                "integrate": True,
                "integration_services": IntegrationSerializer(integrate).data,
                "message": "Se han cargado los datos"
            }
        else:
            data = {
                "integrate": False,
                "integration_services": {},
                "message": "La base de datos ya está poblada, puedes hacer peticiones"
            }
        
        return Response(data)
