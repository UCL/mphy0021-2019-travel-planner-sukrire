from travelplanner.read_passengers import Read_passengers,Read_route
from travelplanner.Passenger import Passenger
from travelplanner.Route import Route
from travelplanner.Journey import Journey
import numpy as np
import pytest

#need to write tests for read passengers

#passenger class tests


def test_Passenger():
    testpassenger = Passenger(start=(0,0),end=(3,4),pace=10)
    testpassengers = Passenger("travelplanner/tests/passenger.csv")
    assert testpassenger.start  == []
    assert testpassenger.end == []
    assert testpassenger.pace == []
    assert testpassenger.specifystart == (0,0)
    assert testpassenger.specifyend == (3,4)
    assert testpassenger.specifypace == 10
    assert testpassengers.start == (2,3)
    assert testpassengers.end == (24,0)
    assert testpassengers.pace == 12
    assert testpassengers.specifystart == None
    assert testpassengers.specifyend == None
    assert testpassengers.specifypace == None
    
def test_walktime():
    testwalktime = Passenger(start=(0,0),end=(3,4),pace=10)
    assert testwalktime.walktime() == 50
    
#route class tests    
# need to write tests for routemap
   
def test_Route():
    testroute = Route("travelplanner/tests/route.csv")
    assert testroute.bstop[0] == 'A'
    with pytest.raises(AssertionError):
        wrong_route = Route("travelplanner/tests/route_wrong.csv")
    
def test_timetimetable():
    testroute = Route("travelplanner/tests/route.csv")
    assert(testroute.timetable()[12]) == ('B', 120, 12)
    
#journey class tests
#need to add tests for other 2 functions

def test_Journey():
    journeytest=Journey("travelplanner/tests/route.csv","travelplanner/tests/passenger.csv",speed=10)
    assert journeytest.stops == [0, 12, 17, 18, 19, 22, 25]
    
def test_travel_time():
    jtesttt=Journey("travelplanner/tests/route.csv","travelplanner/tests/passenger.csv")
    assert jtesttt.travel_time()[1] == ['266.4432397340942', '0']

def test_print_time_stats():
    jtestpts = Journey("travelplanner/tests/route.csv","travelplanner/tests/passenger.csv")
    jtestpts.print_time_stats()
    assert (jtestpts.total_time_on_bus/jtestpts.bus_pass) == 0
    assert round(jtestpts.total_time_walking/jtestpts.walker,2) == 194.44
    
