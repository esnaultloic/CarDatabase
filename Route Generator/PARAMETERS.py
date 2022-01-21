import uuid
import random
import requests
import json
import numpy as np
import cProfile
import re


class Parameters:
    """ Entries parameters of the Truck Data Generator
    
    :param mu: Mean consumption in L/100km, defaults to None
    :type mu: float or None
    :param sigma: Standard deviation of the normal low for the consumption, defaults to None
    :type sigma: float or None
    :param iterations: Number of truck to generate, defaults to None
    :type iterations: int or None
    :param list_energy: List of the different type of energy, defaults to None
    :type list_energy: list[str] or None
    :param list_speedprofile: List of the speed profile type, defaults to None
    :type list_speedprofile: list[str] or None
    :param list_route_pm: List to set-up the route of the type ['behavior=[fastest,shortest];type_of_vehicule=[truck];traffic:default'], defaults to None
    :type list_route_pm: list[str] or None
    """
    def __init__(self, mu, sigma,iterations, list_energy, list_speedprofile, list_route_pm) -> None:
        self.mu = mu
        self.sigma = sigma
        iterations = iterations
        self.list_energy = list_energy
        self.list_speedprofile = list_speedprofile
        self.list_route_pm = list_route_pm
        self.list_comsumption = list(np.random.normal(mu, sigma, iterations))

    def def_parameters(self):
        parameters = {"mu": self.mu,
                      "sigma": self.sigma,
                      "list_energy": self.list_energy,
                      "list_speedprofile": self.list_speedprofile,
                      "list_route_pm": self.list_route_pm,
                      "list_comsumption": self.list_comsumption}
        return parameters
