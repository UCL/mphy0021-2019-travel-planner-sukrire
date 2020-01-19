import numpy as np
import math
import matplotlib.pyplot as plt
from travelplanner.Passenger import Passenger
from travelplanner.Route import Route


class Journey:  
    
	def __init__(self,route,passenger,passno=0, speed=10):
		self.route = Route.Route(route,speed)
		self.passenger = Passenger.Passenger(passenger,passno)
		self.timetable= Route.Route.timetable(self.route)
		self.stops = [step[2] for step in self.timetable if step[0]]
		
	def plot_bus_load(self):
		self.value = {value[2]:0 for value in self.timetable if value[0]}
		self.stoplabels = [step[0] for step in self.timetable if step[0]]
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
		
	def travel_time(self):
		list_walktime = ['Walk time']
		list_bustime = ['Bus time']
		self.passid = np.linspace(0,len(self.passenger.passengers),len(self.passenger.passengers)+1,dtype=int)
		for passno in range(len(self.passenger.passengers)):
			time_to_walk = self.passenger_trip_time(passno)[0]
			time_on_bus = self.passenger_trip_time(passno)[1]
			if time_to_walk+time_on_bus == 0:
				list_walktime.append(self.passenger.walktime(passno))
				list_bustime.append(0)
			else:
				list_walktime.append(time_to_walk)
				list_bustime.append(time_on_bus)
		self.traveldic = dict(zip(self.passid, map(list, zip(map(str,list_walktime ), map(str, list_bustime)))))
		return self.traveldic

	def print_time_stats(self):
		self.total_time_on_bus=0
		self.total_time_walking=0
		self.bus_pass=0
		self.walker=0
		for commuter in range(len(self.passenger.passengers)):
			self.total_time_walking += float(self.travel_time()[commuter+1][0])
			self.total_time_on_bus += float(self.travel_time()[commuter+1][1])
			if float(self.travel_time()[commuter+1][1]) != 0:
				self.bus_pass += 1
			if float(self.travel_time()[commuter+1][0]) != 0:
				self.walker += 1
		if self.bus_pass == 0:
			self.bus_pass=1
		print ("Average time spent on bus:" ,self.total_time_on_bus/self.bus_pass,"\n","Average time spent walking:" ,round(self.total_time_walking/self.walker,2))
		
	def passenger_trip(self,testpass):
		# calculate closer stops
		## to start
		self.distances = [(math.sqrt((self.route.xcoord[stop] - self.passenger.passengers[testpass][0][0])**2 + (self.route.ycoord[stop] - self.passenger.passengers[testpass][0][1])**2), stop) for stop in self.stops]
		closer_start = min(self.distances)
		## to endRoute.
		self.distances = [(math.sqrt((self.route.xcoord[stop] - self.passenger.passengers[testpass][1][0])**2 + (self.route.ycoord[stop] - self.passenger.passengers[testpass][1][1])**2), stop) for stop in self.stops]
		closer_end = min(self.distances)
		return (closer_start, closer_end)

	def passenger_trip_time(self,testpass):
		bus_times = [row[1] for row in self.timetable]
		bus_travel = bus_times[self.passenger_trip(testpass)[1][1]] - bus_times[self.passenger_trip(testpass)[0][1]]
		walk_travel = self.passenger_trip(testpass)[0][0] * self.passenger.pace + self.passenger_trip(testpass)[1][0] * self.passenger.pace
		if (bus_travel+walk_travel) >= self.passenger.walktime(testpass) or bus_travel <= 0:
			return (0,0)
		else:
			return (walk_travel,bus_travel)
    