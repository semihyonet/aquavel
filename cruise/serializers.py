from rest_framework import serializers
from cruise.models import Port, Cruise, CruiseRoute

# Used to initialize Cruise Ships and it's routes
class CruiseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)

    port = serializers.ListSerializer(min_length=2,
                                      allow_empty=False,
                                      child=serializers.CharField(max_length=32, min_length=1))

    starting_date = serializers.DateField(format="dd/mm/yyyy")




class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ["name"]


class CruiseRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CruiseRoute
        fields = ["departure_date", "arrival_date", "arrival_port", "cruise", "departure_port"]
