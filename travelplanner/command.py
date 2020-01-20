from argparse import ArgumentParser
from travelplanner.read_passengers import Read_passengers,Read_route
from travelplanner.Passenger import Passenger
from travelplanner.Route import Route
from travelplanner.Journey import Journey
import numpy as np
import matplotlib.pyplot as plt

import travelplanner


def process():

    parser = ArgumentParser(description='travelplanner')
    parser.add_argument('routefile', type=str, help='Please give full pathname to route.csv')
    parser.add_argument('passfile', type=str, help='Please give full pathname to passenger.csv')
    parser.add_argument('--speed', default=10, type=int, help='Give the speed of the bus, lower is faster')
    parser.add_argument('--saveplots', default=False,help='Optional.If given,save the two plots.')

    arguments = parser.parse_args()

   # need to print passenger travel time and average time on bus total
    passengers_for_times = travelplanner.Journey(arguments.routefile,arguments.passfile,speed=arguments.speed)
    route_for_timetable = travelplanner.Route(arguments.routefile, speed=arguments.speed)
    timetable=route_for_timetable.timetable()
    stoptimes=[stop[1] for stop in timetable if stop[0]]
    stoplabels=[label[0] for label in timetable if label[0]]
    
    for i in range(len(stoptimes)):
        print("Bus Stop:",stoplabels[i],"Bus will arrive at",stoptimes[i],"mins")
    for j in range(len(passengers_for_times.passenger.passengers)):
        if passengers_for_times.passenger_trip_time(j)[1] == 0 :
            print("Passenger no:",[j+1], "will walk for", passengers_for_times.travel_time()[j][0], "mins")
        else:
            print("Passenger no:",[j+1], "will get on at stop:", 
            passengers_for_times.timetable[passengers_for_times.passenger_trip(j)[0][1]][0],
            "and will get off at stop",
            passengers_for_times.timetable[passengers_for_times.passenger_trip(j)[1][1]][0], "\n"
            ,"they will walk for:",passengers_for_times.travel_time()[i][0], "mins", "\n"
            , "and will be on the bus for",passengers_for_times.travel_time()[i][1], "mins" )
    

    if arguments.saveplots:
        # Plots the route of the bus
        route_map = route_for_timetable.plot_map()
        plt.show()
        route_map.savefig('./map.png')
        # Plots the number of passenger on the bus
        bus_load_map = passengers_for_times.plot_bus_load()
        bus_load_map.savefig('./load.png')


if __name__ == "__main__":
    process()
