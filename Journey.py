

def plot_bus_load(route, passengers):
    stops = {step[2]:0 for step in route if step[2]}
    for j in range(len(passengers)):
        trip = passenger_trip(passengers[j], route)
        stops[trip[0][1]] += 1
        stops[trip[1][1]] -= 1
    for i, stop in enumerate(stops):
        if i > 0:
            stops[stop] += stops[prev]
        prev = stop
    fig, ax = plt.subplots()
    ax.step(range(len(stops)), list(stops.values()), where='post')
    ax.set_xticks(range(len(stops)))
    ax.set_xticklabels(list(stops.keys()))
    plt.show()
    
def passenger_trip(passenger, route):
    start, end, pace = passenger
    stops = [value for value in route if value[2]]
    # calculate closer stops
    ## to start
    distances = [(math.sqrt((x - start[0])**2 + (y - start[1])**2), stop) for x,y,stop in stops]
    closer_start = min(distances)
    ## to end
    distances = [(math.sqrt((x - end[0])**2 + (y - end[1])**2), stop) for x,y,stop in stops]
    closer_end = min(distances)
    return (closer_start, closer_end)

def passenger_trip_time(passenger, route):
    walk_distance_stops = passenger_trip(passenger, route)
    bus_times = timetable(route)
    bus_travel = bus_times[walk_distance_stops[1][1]] - \  bus_times[walk_distance_stops[0][1]]
    walk_travel = walk_distance_stops[0][0] * passenger[2] + \ walk_distance_stops[1][0] * passenger[2]
    return bus_travel + walk_travel
    
    
for i in range(len(passgens)):
    print(f"Trip for passenger: {passenger_id[i]}")
    start, end = passenger_trip(genpassenger[i], route2)
    total_time = passenger_trip_time(genpassenger[i], route2)
    print((f" Walk {start[0]:3.2f} units to stop {start[1]}, \n"
    f" get on the bus and alite at stop {end[1]} and \n"
    f" walk {end[0]:3.2f} units to your destination."))
    print(f" Total time of travel: {total_time:03.2f} minutes")