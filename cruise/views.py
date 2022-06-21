import datetime

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from cruise.serializers import CruiseSerializer

from cruise.models import Port, Cruise, CruiseRoute

class CruiseAPI(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CruiseShipAPI(APIView):
    """
    This Methos is mainly used to seed the database.
    """
    def post(self, request):
        serializer = CruiseSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        cruise_ports = serializer.validated_data.get("port")

        port_objects = []

        # Get or Create Port objects
        for port_name in cruise_ports:
            port_object, created = Port.objects.get_or_create(name=port_name)

            port_objects.append(port_object)

        new_cruise_ship = Cruise(cruise_line_name=serializer.validated_data.get("name"))
        new_cruise_ship.save()

        starting_date: datetime.date = serializer.validated_data.get("starting_date")

        # Create Cruise Routes for Cruise
        for i in range(len(port_objects) - 1):
            new_cruise_route = CruiseRoute(
                cruise=new_cruise_ship,
                departure_port=port_objects[i],
                arrival_port=port_objects[i+1],
                departure_date=starting_date,
                arrival_date=starting_date+datetime.timedelta(days=1)
               )

            new_cruise_route.save()

            # Add 1 day to the starting date for the next cruise route
            starting_date += datetime.timedelta(days=1)

        return Response("Completed")
