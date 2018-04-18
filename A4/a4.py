from pymongo import MongoClient
from multiprocessing import Lock, Process
import time

client= MongoClient()
db=client.dbname

def read_food(name):
	doc=db.coll.find_one({'phil':name})
	food=doc["food"]
	return food
	
class Philosopher(Process):
	name=""
	food=""
	lock1=None
	lock2=None

	def __init__(self, name, lock1, lock2):
		super(Philosopher, self).__init__()
		self.name=name
		self.food=read_food(name)
		self.lock1=lock1
		self.lock2=lock2
	def run(self):
		while True:
			print self.name, "is thinking"
			time.sleep(2)
			print self.name, "wants to eat"
			lock1.acquire()
			lock2.acquire()
			print self.name, "is eating"
			time.sleep(2)
			print self.name, "has finished eating"
			lock1.release()
			lock2.release()

locks=[Lock() for i in range(5)]

for i in range(5):
	lock1=locks[i]
	lock2=locks[(i+1)%5]
	p=Philosopher(str(i), lock1, lock2)
	p.start()