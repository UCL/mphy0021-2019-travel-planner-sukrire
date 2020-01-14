import numpy as np
from read_passengers import Read_passengers

pathpassenger = input("path to passenger\n> ")
i= int(input("which passenger\n> "))
#pathpassenger = "passenger.csv"

class Passenger:

    start=[]
    stop=[]
    pace=[]

    passengers,passenger_id=Read_passengers(pathpassenger)
    start,stop,pace = passengers[i] 

    def __init__(self,start,stop,pace):
        self.start = start
        self.stop = stop
        self.pace = pace
    
    
    def walktime(self):
        return np.sqrt((self.start[0]-self.stop[0])**2+(self.start[1]-self.stop[1])**2)*self.pace
    