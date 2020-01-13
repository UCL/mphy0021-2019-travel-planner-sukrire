def timetable(route):
'''
Generates a timetable for a route as minutes from its first stop.
'''
time = 0
stops = {}
for step in route:
if step[2]:
stops[step[2]] = time
time += 10
return stops
In this city, passengers can walk in straight lines from one point to another. Therefore, they can walk from
one point to another without worrying about the grid. A passenge’sr walking distance to the closest starting
and ending stop is then calculated as:
def passenger_trip(passenger, route):
start, end, pace = passenger
stops = [value for value in route if value[2]]
# calculate closer stops
## to start
distances = [(math.sqrt((x - start[0])**2 +
(y - start[1])**2), stop) for x,y,stop in stops]
closer_start = min(distances)
## to end
distances = [(math.sqrt((x - end[0])**2 +
(y - end[1])**2), stop) for x,y,stop in stops]
closer_end = min(distances)
return (closer_start, closer_end)
Think, however, what happens when two stops are at the same distance! Or when the order of the closest
stops does not match the direction of travel!
The total travel time for a particular passenger can be obtained using the following function:
def passenger_trip_time(passenger, route):
walk_distance_stops = passenger_trip(passenger, route)
bus_times = timetable(route)
bus_travel = bus_times[walk_distance_stops[1][1]] - \
bus_times[walk_distance_stops[0][1]]
walk_travel = walk_distance_stops[0][0] * passenger[2] + \
walk_distance_stops[1][0] * passenger[2]
return bus_travel + walk_travel
Although that function gives you the total travel time, you probably would prefer to know how much of that
time is by foot and how much is on the bus.
Finally, we also have some visualisation tools. One displays the route and the stops on a grid:
def plot_map(route):
max_x = max([n[0] for n in route]) + 5 # adds padding
max_y = max([n[1] for n in route]) + 5
grid = np.zeros((max_y, max_x))
for x,y,stop in route:
grid[y, x] = 1
if stop:
grid[y, x] += 1
fig, ax = plt.subplots(1, 1)
ax.pcolor(grid)
ax.invert_yaxis()
2
ax.set_aspect('equal', 'datalim')
plt.show()
Another function displays the number of people on the bus between stops:
def plot_bus_load(route, passengers):
stops = {step[2]:0 for step in route if step[2]}
for passenger in passengers.values():
trip = passenger_trip(passenger, route)
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
With all these functions we can then generate some output with:
print(" Stops: minutes from start\n", timetable(route))
for passenger_id, passenger in passengers.items():
print(f"Trip for passenger: {passenger_id}")
start, end = passenger_trip(passenger, route)
total_time = passenger_trip_time(passenger, route)
print((f" Walk {start[0]:3.2f} units to stop {start[1]}, \n"
f" get on the bus and alite at stop {end[1]} and \n"
f" walk {end[0]:3.2f} units to your destination."))
print(f" Total time of travel: {total_time:03.2f} minutes")
# Plots the route of the bus
plot_map(route)
# Plots the number of passenger on the bus
plot_bus_load(route, passengers)
Stops: minutes from start
{'A': 0, 'B': 50, 'C': 100, 'D': 150, 'E': 230, 'F': 260, 'G': 310}
Trip for passenger: 1
Walk 2.24 units to stop A,
get on the bus and alite at stop B and
walk 1.00 units to your destination.
Total time of travel: 98.54 minutes
...
Busses can’t move diagonally, only horizontally or vertically. To check for that, you can convert the route
into a chain code and find whether there are odd numbers on it. A chain code is a compressed way to
represent data in image processing. Here’s a simple implementation of it that you may find useful when
checking whether a bus route is valid or not.
def route_cc(route):
'''
Converts a set of route into a Freeman chain code
3 2 1
\ | /
4 - C - 0
/ | \
5 6 7
'''
3
start = route[0][:2]
cc = []
freeman_cc2coord = {0: (1, 0),
1: (1, -1),
2: (0, -1),
3: (-1, -1),
4: (-1, 0),
5: (-1, 1),
6: (0, 1),
7: (1, 1)}
freeman_coord2cc = {val: key for key,val in freeman_cc2coord.items()}
for b, a in zip(route[1:], route):
x_step = b[0] - a[0]
y_step = b[1] - a[1]
cc.append(str(freeman_coord2cc[(x_step, y_step)]))
return start, ''.join(cc)
and this is how to use it:
start_point, cc = route_cc(route)
print((f"The bus route starts at {start_point} and\n"
f"it's described by this chain code:\n{cc}"))
The bus route starts at (2, 1) and
it's described by this chain code:
0000060000200066644444660000000
2