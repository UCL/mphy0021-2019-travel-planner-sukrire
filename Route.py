import numpy as np
import matplotlib.pyplot as plt
from read_passengers import Read_route

#pathroute = input("path to route\n> ")

pathroute = "route.csv"

route=Read_route(pathroute)
xcoord=[]
ycoord=[]
bstop=[]
stopno=[]

for points in range(len(route)):
    xcoord.append(route[points][0])
    ycoord.append(route[points][1])
    bstop.append(route[points][2])


class Route:


    def __init__(self,xcoord,ycoord,bstop): 
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.bstop = bstop
                
       
    def timetable(self):
        
        time=0
        for tick in range(len(self.bstop)):
            if self.bstop[tick] != '':
                stopno.append(time)
            else: 
                stopno.append('')
            time+= 10
        return stopno,self.bstop     
  
      
    def plot_map(self):
        max_x = max([n for n in self.xcoord]) + 5 # adds padding
        max_y = max([n for n in self.ycoord]) + 5
        grid = np.zeros((max_y, max_x))
        for stop in self.bstop:
            grid[self.ycoord,self.xcoord] = 1
            if stop != ' ':
                grid[self.ycoord,self.xcoord] += 1
        fig, ax = plt.subplots(1, 1)
        ax.pcolor(grid)
        ax.invert_yaxis()
        ax.set_aspect('equal', 'datalim')
        plt.show()

    def route_cc(self):
        '''
        Converts a set of route into a Freeman chain code
        3 2 1
        \ | /
        4 - C - 0
        / | \
        5 6 7
        '''
        start = self.xcoord[0],self.ycoord[0]
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

