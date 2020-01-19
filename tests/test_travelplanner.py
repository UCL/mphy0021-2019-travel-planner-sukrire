from travelplanner.read_passengers import read_passengers
from travelplanner.Passenger import Passenger
from travelplanner.Route import Route
from travelplanner.Journey import Journey
import pytest

#passenger class tests

def Passenger():
    testpassenger = Passenger(start=(0,0),end=(3,4),pace=10)
    testpassengers = Passenger("passenger.csv")
    assert testpassenger.start  == []
    assert testpassenger.end == []
    assert testpassenger.pace == []
    assert testpassenger.specifystart == (0,0)
    assert testpassenger.specifyend == (3,4)
    assert testpassenger.specifypace == 10
    assert testpassengers.start == (2,3)
    assert testpassengers.end == (24,0)
    assert testpassengers.pace == 10
    assert testpassengers.specifystart == None
    assert testpassengers.specifyend == None
    assert testpassengers.specifypace == None
    
def test_walk_time():
    testwalktime= Passenger(start=(0,0),end=(3,4),pace=10)
    assert testwalktime.walk_time() == 50
    
#route class tests    
    
def Route():
    testroute = Route("route.csv")
    assert testroute.bstop[0] == 'A'
    assert(Route("route_wrong.csv")) =  'Diagonal route'   
    
def timetimetable():
    testroute = Route("route.csv")
    assert(testroute.timetable()[12]) == ('B', 120, 12)
    
#journey class tests

def Journey():
    journeytest=Journey("route.csv","passenger.csv",speed=10)
    assert journeytest.stops == [0, 12, 17, 18, 19, 22, 25]
    
def travel_time():
    jtesttt=Journey("route.csv","passenger.csv")
    assert jtesttt.travel_time()[1] == ['266.4432397340942', '0']

def print_time_stats():
    jtestpts = Journey("route.csv","passenger.csv")
    jtestpts.print_time_stats()
    assert (jtestpts.total_time_on_bus/jtestpts.bus_pass) == 0
    assert round(jtestpts.total_time_walking/jtestpts.walker,2) == 194.44
    
