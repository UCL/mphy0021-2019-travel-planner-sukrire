import numpy as np
from read_passengers import Read_passengers

#pathpassenger = input("path to passenger\n> ")
i= int(input("which passenger\n> "))
pathpassenger = "passenger.csv"



start=[]
end=[]
pace=[]

passengers,passenger_id=Read_passengers(pathpassenger)
start,end,pace = passengers[i] 


class Passenger:


    def __init__(self,start,end,pace):
        self.start = start
        self.end = end
        self.pace = pace
    
    
    def walktime(self):
        return np.sqrt((self.start[0]-self.end[0])**2+(self.start[1]-self.end[1])**2)*self.pace
    