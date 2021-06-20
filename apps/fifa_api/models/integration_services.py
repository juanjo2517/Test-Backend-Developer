""" IntegrationServices """
# Django
from django.db import models

# Utils 
from core.utils.model import CuembyModel

class IntegrationServices(CuembyModel):
    already_integrated = models.BooleanField(default=False)
    start_integration = models.DateTimeField(auto_now=False, auto_now_add=False)
    finish_integration = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    class Meta:
        db_table = "integration_services"
        verbose_name = "Integración con el Servicio FIFA"
        verbose_name_plural = "Integración con el Servicio FIFA"
    

    def __str__(self):
        return "{} - {} - {}".format(
            self.already_integrated,
            self.start_integration,
            self.finish_integration
        )