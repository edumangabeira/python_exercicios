from types import *

class MyDB:


	def __init__(self, id, name):
		self.id = id
		self.name = name


	def __str__(self):
		print(self.id)
		print(self.name)
		assert isinstance(self.id, int), f"id is not an integer: {self.id}"
		assert isinstance(self.name, str), f"name is not a string: {self.name}"


	def __repr__(self):
		print(self.id)
		print(self.name)
		assert isinstance(self.id, int), f"id is not an integer: {self.id}"
		assert isinstance(self.name, str), f"name is not a string: {self.name}"

obj = MyDB(4760,'ronaldo')
print(obj)
