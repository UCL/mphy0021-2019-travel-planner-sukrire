import numpy as np

pathroute = raw_input("path to route\n> ")
routegentext= np.genfromtxt(pathroute, delimiter=",",dtype='unicode')
pathpassenger = raw_input("path to passenger\n> ")
passgentext= np.genfromtxt(pathpassenger, delimiter=",",dtype='unicode')


route=[]
for i in range(len(route)):
    route.append((int(route[i,0]),int(route[i,1]),(route[i,2])))
    
passengers=[]    
for i in range(len(passengers)):
    passengers.append(((passgentext[i,0],passgentext[i,1]),(passgentext[i,2],passgentext[i,3]),(passgentext[i,4])))

passenger_id=np.linspace(1,len(passgens),len(passgens))