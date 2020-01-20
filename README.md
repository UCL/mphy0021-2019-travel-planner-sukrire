# mphy0021-2019-travel-planner-sukrire

To install, use pip install "path to tar"
To run in command line use:

bussimula routefile routepass --speed SPEED --saveplots

This will print out who will walk and who will use the bus and how fast each journey is.
The SPEED will default to 10 if not specified and the --saveplots will save 2 images of 
the route and the bus load in the install directory.

To use in a .py file:

from travelplanner import Class

Where Class can be Passenger, Journey or Route.

Then create a passenger, journey or route by:

singlepassenger = Passenger(start=(10,15), end=(20,20), speed=15)
passengers= Passenger("destinationfile.csv")


route= Route("destinationfile.csv", speed=10)

note, speed is an optional argument and will default to 10

journey=Journey("routefile.csv","passfile.csv")

with similar optional arguments. 

To run functions call them as classes.


