import uuid
import random
import requests
import json
import numpy as np
import cProfile
import re


class API:   
    """ Route Input
    
    :param waypoint0: Starting point of the route with the form "lat,long", defaults to None
    :type waypoint0: str or None
    :param waypoint1: Ending point of the route with the form "lat,long", defaults to None
    :type waypoint1: str or None
    :param vehicletype: Type of energy concatenate with Consumption L/100km, defaults to None
    :type vehicletype: str or None
    :param speedprofile: Behavior of the driver "fast" or "default", defaults to None
    :type speedprofile: str or None
    :param mode: List to set-up the route of the type ['behavior=[fastest,shortest];type_of_vehicule=[truck];traffic:default'], defaults to None
    :type mode: list[str]
    """
    def __init__(self, waypoint0, waypoint1, vehicletype, speedprofile, mode) -> None:
        self.waypoint0 = waypoint0
        self.waypoint1 = waypoint1
        self.vehicletype = vehicletype
        self.speedprofile = speedprofile
        self.mode = mode

    def call(self, KEY):
        """ Call the Here API 
        
        :param KEY: API KEY to be connected to the Here API, defaults to None
        :type KEY: str or None
        :return: Response of the API call
        :rtype: json
        """
        params = (
            ('apiKey', KEY),
            ('waypoint0', self.waypoint0),
            ('waypoint1', self.waypoint1),
            ('vehicletype', self.vehicletype),
            ('speedprofile', self.speedprofile),
            ('mode', self.mode),
        )
        response = requests.get(
            'https://route.ls.hereapi.com/routing/7.2/calculateroute.json', params=params)
        return response.json()
