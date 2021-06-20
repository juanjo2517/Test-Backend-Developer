""" Funciones para guardar los equipos y jugadores """

# Models
from apps.fifa_api.models import Player, Team


def save_teams(data, page):
    """ Funcion para guardar equipos en BD
        :data objeto JSON del jugador que viene de la API
        :page pagina en la que aparece en la API
    """
    
    # Ver si hay un equipo que exista con los datos entrantes
    team = Team.objects.filter(name=data['club']['name']).first()

    # Bool para saber si es registro nuevo
    is_new = False

    # Si no existe se guarda, de lo contrario retorna el equipo seleccionado
    if not team:
        new_team = Team.objects.create(
            name=data['club']['name'],
            league=data['league']['name'],
            page_saved = page
        )

        is_new = True
        return new_team, is_new
    else:
        team, is_new


def save_players(data, page, team):
    """ Funcion para guardar jugadores en BD 
        :data objeto JSON del jugador que viene de la API
        :page pagina en la que aparece en la API
        :team Equipo al que pertenece el jugador
    """
    
    # Ver si hay un jugador que exista con los datos entrantes
    player = Player.objects.filter(
        first_name = data['firstName'],
        last_name = data['lastName'],
        position = data['position'],
        nacionality = data['nation']['name'],
        team = team.id
    ).first()

    # Bool para saber si es registro nuevo
    is_new = False

    # Si no existe se guarda, de lo contrario retorna el equipo seleccionado
    if not player:
        new_player = Player.objects.create(
            first_name = data['firstName'],
            last_name = data['lastName'],
            position = data['position'],
            nacionality = data['nation']['name'],
            team = team
        )

        is_new = True
        return new_player, is_new
    else:
        return player, is_new