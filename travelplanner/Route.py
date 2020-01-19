import numpy as np
import matplotlib.pyplot as plt
from travelplanner.read_passengers import Read_route

class Route:

    def __init__(self,route, speed=10): 
        self.speed = speed                     
        self.route = Read_route(route)
        self.xcoord=[]
        self.ycoord=[]
        self.bstop=[]
        for points in range(len(self.route)):
            self.xcoord.append(self.route[points][0])
            self.ycoord.append(self.route[points][1])
            self.bstop.append(self.route[points][2]) 
        route_cc=self.route_cc()
        for i in route_cc[1]:
            assert int(i) % 2 == 0, 'Diagonal route'
       
    def timetable(self):
        self.stoptime=[]
        self.timetablevec=[]
        self.stopno=[]
        time=0
        stopcount=0
        for tick in range(len(self.bstop)):
            if self.bstop[tick] != '':
                self.stoptime.append(time)
                self.stopno.append(stopcount)
            else: 
                self.stoptime.append('')
                self.stopno.append('')
            time+= self.speed
            stopcount+= 1
        for points in range(len(self.bstop)):
            self.timetablevec.append((self.bstop[points],self.stoptime[points],self.stopno[points]))
        return self.timetablevec    
  
      
    def plot_map(self):
        self.stopmarks = [step[2] for step in self.timetable() if step[0]]
        max_x = max([n for n in self.xcoord]) + 5 # adds padding
        max_y = max([n for n in self.ycoord]) + 5
        grid = np.zeros((max_y, max_x))
        for stop in self.bstop:
            grid[self.ycoord,self.xcoord] = 1
        for stop in self.stopmarks:
                grid[self.ycoord[self.timetable()[stop][2]],self.xcoord[self.timetable()[stop][2]]] += 1
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
        for b, a in zip(self.route[1:], self.route):
            x_step = b[0] - a[0]
            y_step = b[1] - a[1]
            cc.append(str(freeman_coord2cc[(x_step, y_step)]))
        return start, ''.join(cc)

