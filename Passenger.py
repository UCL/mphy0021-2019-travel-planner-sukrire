import numpy as np
from read_passengers import Read_passengers

class Passenger:

	def __init__(self, pathpassenger = None, passno=0 ,start=None,end=None,pace=None):
		self.start = []
		self.end = []
		self.pace = []
		self.specifystart = start
		self.specifyend = end
		self.specifypace = pace
		self.pathpassenger = pathpassenger
		if self.pathpassenger is not None:
			self.passengers=Read_passengers(pathpassenger)
			self.start,self.end,self.pace = self.passengers[passno]
   
	def walktime(self, pathpassenger):
		if pathpassenger is None:
			self.start = self.specifystart
			self.end = self.specifyend
			self.pace = self.specifypace
		return np.sqrt((self.start[0]-self.end[0])**2+(self.start[1]-self.end[1])**2)*self.pace
    