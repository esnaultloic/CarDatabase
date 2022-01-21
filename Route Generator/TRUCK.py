import uuid
import random
import requests
import json
import numpy as np
import cProfile
import re


class Truck:
    """ Truck Data Generator 
    
    :param name: Name of the truck, defaults to None
    :type name: str or None
    :param energy: Type of energy used by the truck, defaults to None
    :type energy: str or None
    :param consumption: Concumption in L/100km, defaults to None
    :type consumption: float or None
    :param speedprofile: , defaults to None
    :type speedprofile: str or None
    :param mode: List to set-up the route of the type ['behavior=[fastest,shortest];type_of_vehicule=[truck];traffic:default'], defaults to None
    :type mode: list[str] or None
    """
    def __init__(self, name, energy, consumption, speedprofile, mode) -> None:
        self.name = name
        self.energy = energy
        self.consumption = consumption
        self.id = str(uuid.uuid4())
        self.vehicletype = (self.energy+","+str(self.consumption))
        self.speedprofile = speedprofile
        self.mode = mode

    def create_truck(self):
        truck_data = {"name": self.name,
                      "energy": self.energy,
                      "consumption": self.consumption,
                      "vehicletype": self.vehicletype,
                      "speedprofile": self.speedprofile,
                      "route_pm": self.mode,
                      "id": self.id}
        return truck_data
