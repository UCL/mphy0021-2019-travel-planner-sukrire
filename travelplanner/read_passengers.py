import numpy as np


def Read_passengers(pathpassenger):
    passgentext = np.genfromtxt(pathpassenger, delimiter=",", dtype='int')
    passengers = []
    for j in range(len(passgentext)):
        passengers.append(((passgentext[j, 0], passgentext[j, 1]),
                           (passgentext[j, 2], passgentext[j, 3]),
                           (passgentext[j, 4])))
    return passengers


def Read_route(pathroute):
    routegentext = np.genfromtxt(pathroute, delimiter=",", dtype='unicode')
    route = []
    for i in range(len(routegentext)):
        route.append((int(routegentext[i, 0]), int(routegentext[i, 1]),
                     (routegentext[i, 2])))
    return route
