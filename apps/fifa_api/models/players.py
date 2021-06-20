from django.db import models

# Utils 
from core.utils.model import CuembyModel

# Models 
from .team import Team

class Player(CuembyModel):
    
    first_name = models.CharField(max_length = 150, help_text="Primer Nombre del Jugador")
    last_name = models.CharField(max_length = 150, help_text="Posición del Jugador")
    position = models.CharField(max_length = 150, help_text="Posición del Jugador")
    nacionality = models.CharField(max_length = 150, help_text="Nacionalidad del Jugador")
    page_saved = models.CharField(max_length = 5, help_text="Pagina en la que se encuentra en la API")
    
    team = models.ForeignKey(
        Team, 
        on_delete=models.DO_NOTHING,
        related_name='team_player',
        help_text='Equipo en el que juega el jugador'
    )
    

    class Meta:
        db_table = "player"
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
    
    def __str__(self):
        return "{} {} - {}".format(
            self.first_name,
            self.last_name,
            self.team
        )
