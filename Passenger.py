import numpy as np
from read_passengers import Read_passengers

class Passenger:

    def __init__(self,pathpassenger,passno):
        self.start = []
        self.end = []
        self.pace = []
        self.passengers,self.passenger_id=Read_passengers(pathpassenger)
        self.start,self.end,self.pace = self.passengers[passno]
   
    def walktime(self):
        return np.sqrt((self.start[0]-self.end[0])**2+(self.start[1]-self.end[1])**2)*self.pace
    