from django.db import models

# Create your models here.
import core.models


class Port(core.models.AbstractModel):
    name = models.CharField(max_length=32)


class Cruise(core.models.AbstractModel):
    cruise_line_name = models.CharField(max_length=64)


class CruiseRoute(core.models.AbstractModel):
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE)
    departure_port = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='%(class)s_port_created')
    arrival_port = models.ForeignKey(Port, on_delete=models.CASCADE)

    departure_date = models.DateField()
    arrival_date = models.DateField()
