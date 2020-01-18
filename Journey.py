import numpy as np
import math
import matplotlib.pyplot as plt
from Passenger import Passenger 
import Route

class Journey(Passenger):  
    
	def __init__(self,route,speed = 10, passno=0 ,start=None,end=None,pace=None, pathpassenger = None):
		super().__init__(start=start,end=end,pace=pace,pathpassenger=None)
		self.route = Route.Route(route,speed=10)
		self.stops = [step[2] for step in self.route.timetable() if step[0]]
        
	def plot_bus_load(self):
		# calculate closer stops
		## to start
		distances = [(math.sqrt((self.route.xcoord[stop] - self.passenger.passengers[testpass][0][0])**2 + (self.route.ycoord[stop] - self.passenger.passengers[testpass][0][1])**2), stop) for stop in self.stops]
		closer_start = min(self.distances)
		## to endRoute.
		distances = [(math.sqrt((self.route.xcoord[stop] - self.passenger.passengers[testpass][1][0])**2 + (self.route.ycoord[stop] - self.passenger.passengers[testpass][1][1])**2), stop) for stop in self.stops]
		closer_end = min(self.distances)
		self.value = {value[2]:0 for value in self.route.timetable() if value[0]}
		self.stoplabels = [step[0] for step in self.route.timetable() if step[0]]
		for testpass in range(len(self.passenger.passengers)):
			self.value[self.passenger_trip(testpass)[0][1]] += 1
			self.value[self.passenger_trip(testpass)[1][1]] -= 1
		for i, stop in enumerate(self.value):
			if i > 0:
				self.value[stop] += self.value[prev]
			prev = stop
		fig, ax = plt.subplots()
		ax.step(range(len(self.value)), list(self.value.values()), where='post')
		ax.set_xticks(range(len(self.stops)))
		ax.set_xticklabels(list(self.stoplabels))
		plt.show()
		
	def passenger_trip(self):
		distances = [(math.sqrt((self.route.xcoord[stop] - self.specifystart()[0])**2 + (self.route.ycoord[stop] - self.specifystart()[1])**2), stop) for stop in self.stops]
		closer_start = min(self.distances)
		## to endRoute.
		distances = [(math.sqrt((self.route.xcoord[stop] - self.passenger.passengers[testpass][1][0])**2 + (self.route.ycoord[stop] - self.passenger.passengers[testpass][1][1])**2), stop) for stop in self.stops]
		closer_end = min(self.distances)
		return (closer_start, closer_end)

	def passenger_trip_time(self,testpass):
		bus_times = [row[1] for row in self.timetable]
		bus_travel = bus_times[self.passenger_trip(testpass)[1][1]] - bus_times[self.passenger_trip(testpass)[0][1]]
		walk_travel = self.passenger_trip(testpass)[0][0] * self.passenger.pace + self.passenger_trip(testpass)[1][0] * self.passenger.pace
		return bus_travel + walk_travel
    