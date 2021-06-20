""" FifaService 
    Clase para conectarse a la API de FIFA 
    y extraer los datos
"""
from config import settings
import requests



# Utils - Save in BD
from ..save_in_bd import save_teams, save_players

class FifaServices():
    url = settings.URL_API_FIFA
    data = {}

    def connect_api(self, page):
        """ funciona para conectarse a la api 
            :page pagina de la API
        """

        # Configurar URL 
        request_url = self.url.format(
            page
        )

        # Realizar peticion al servicio
        response = requests.get(request_url)

        # Enviar a la variable de la clase
        data_fifa = response.json()
        self.data = data_fifa

    
    def save_data(self):
        """ Funcion para guardar datos en BD
        """

        # Conectarse a la API
        self.connect_api(1)

        data_fifa = self.data

        # Extraer el numero de paginas que hay en la API
        num_pages = data_fifa['totalPages']

        array_teams_saved = []
        array_players_saved = []

        for i in range(1, num_pages):
            # Consultar API con iterador de paginado
            self.connect_api(i)

            fifa_players = self.data

            for player in fifa_players['items']:
                # Guardar equipos
                print(type(player))
                team, is_new_team = save_teams(player, i)

                if is_new_team:
                    array_teams_saved.append(team)

                #Guardar jugadores
                player, is_new_player = save_players(player, i, team)

                if is_new_player:
                    array_players_saved.append(player)
        
        if len(array_players_saved) > 0 or len(array_teams_saved) > 0:
            is_saved_data = True
        else:
            is_saved_data = False
        
        return is_saved_data, len(array_teams_saved), len(array_players_saved)
