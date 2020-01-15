import numpy as np
import matplotlib.pyplot as plt
import Passenger
import Route

class Journey:  
    
    def __init__(self,route,passenger,speed,passno):
        self.route = Route.Route(route,speed)
        self.passenger = Passenger.Passenger(passenger,passno)
        self.stops = {step for step in self.route.bstop if step}

    def plot_bus_load(self):
        for j in range(len(self.passengers)):
            trip = passenger_trip(self)
            self.stops[trip[0][1]] += 1
            self.stops[trip[1][1]] -= 1
        for i, stop in enumerate(self.stops):
            if i > 0:
                self.stops[stop] += self.stops[prev]
            prev = stop
        fig, ax = plt.subplots()
        ax.step(range(len(stops)), list(self.stops.values()), where='post')
        ax.set_xticks(range(len(self.stops)))
        ax.set_xticklabels(list(self.stops.keys()))
        plt.show()
        
    def passenger_trip(self):
        # calculate closer stops
        ## to start
        distances = [(math.sqrt((Route.xcoord - Passenger.start[0])**2 + (Route.ycoord - Passemger.start[1])**2), stop) for stop in Route.bstop]
        closer_start = min(distances)
        ## to end
        distances = [(math.sqrt((Route.xcoord - Passenger.end[0])**2 + (Route.ycoord - Passenger.end[1])**2), stop) for stop in Route.bstop]
        closer_end = min(distances)
        return (closer_start, closer_end)

    def passenger_trip_time(self):
        walk_distance_stops = self.passenger_trip()
        bus_times = self.timetable()
        bus_travel = bus_times[walk_distance_stops[1][1]] - bus_times[walk_distance_stops[0][1]]
        walk_travel = walk_distance_stops[0][0] * passenger[2] + walk_distance_stops[1][0] * passenger[2]
        return bus_travel + walk_travel
    