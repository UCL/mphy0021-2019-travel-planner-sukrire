import numpy as np
'''
pathroute = raw_input("path to route\n> ")
routegentext= np.genfromtxt(pathroute, delimiter=",",dtype='unicode')
pathpassenger = raw_input("path to passenger\n> ")
passgentext= np.genfromtxt(pathpassenger, delimiter=",",dtype='unicode')
'''
 
def Read_passengers(pathroute,pathpassenger):

    routegentext= np.genfromtxt(pathroute, delimiter=",",dtype='unicode')
    passgentext= np.genfromtxt(pathpassenger, delimiter=",",dtype='int')
    
    route=[]
    for i in range(len(routegentext)):
        route.append((int(routegentext[i,0]),int(routegentext[i,1]),(routegentext[i,2])))
        
    passengers=[]    
    for j in range(len(passgentext)):
        passengers.append(((passgentext[j,0],passgentext[j,1]),(passgentext[j,2],passgentext[j,3]),(passgentext[j,4])))

    passenger_id=np.linspace(1,len(passgentext),len(passgentext))

    return route,passengers,passenger_id

