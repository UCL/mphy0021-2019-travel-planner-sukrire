


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
    ax.set_aspect('equal', 'datalim')
    plt.show()

def route_cc(route):
    '''
    Converts a set of route into a Freeman chain code
    3 2 1
    \ | /
    4 - C - 0
    / | \
    5 6 7
    '''
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

start_point, cc = route_cc(route)
print((f"The bus route starts at {start_point} and\n"
f"it's described by this chain code:\n{cc}"))