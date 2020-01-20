import numpy as np
from travelplanner.read_passengers import Read_passengers


class Passenger:

    def __init__(self, pathpassenger=None, passno=0, start=None, end=None,
                 pace=None):
        self.start = []
        self.end = []
        self.pace = []
        self.specifystart = start
        self.specifyend = end
        self.specifypace = pace
        if pathpassenger is not None:
            self.passengers = Read_passengers(pathpassenger)
            self.start, self.end, self.pace = self.passengers[passno]

    def walktime(self, passno=None):
        if passno is None:
            walkstart = self.specifystart
            walkend = self.specifyend
            walkpace = self.specifypace
        else:
            walkstart, walkend, walkpace = self.passengers[passno]
        return np.sqrt((walkstart[0] - walkend[0])**2 +
                       (walkstart[1] - walkend[1])**2)*walkpace
