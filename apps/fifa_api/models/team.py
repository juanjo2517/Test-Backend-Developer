from django.db import models

# Utils 
from core.utils.model import CuembyModel

class Team(CuembyModel):
    
    name = models.CharField(max_length = 150, help_text='Nombre del equipo')
    league = models.CharField(max_length = 150, help_text='Liga en la que juega el equipo')
    page_saved = models.CharField(max_length = 5, help_text="Pagina en la que se encuentra en la API")

    class Meta:
        db_table = "team"
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
    
    def __str__(self):
        return "{} - {}".format(
            self.name,
            self.league
        )
    
    
    
