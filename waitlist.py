import random

class Student:
	def __init__(self, first, last):
		self.first = first
		self.last = last
		self.sid = random.randint(4000000, 4999999)

	def __str__(self):
		return self.first + " " + self.last

	def get_id(self):
		return self.sid

class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

class Queue:
	def __init__(self):
		self.head = None
		self.size = 0

	def pop_left(self):
		if not self.head:
			return None
		current_head = self.head
		self.head = self.head.next
		self.size -= 1

		print(current_head.data.first + " " + current_head.data.last + " ID: " + str(current_head.data.sid) + " has been moved off the waitlist.")
		print()

		return current_head.data

	def add(self, item):
		new_node = Node(item)

		if not self.head:
			self.head = new_node
		else:
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = new_node
		self.size += 1

	def is_empty(self):
		if self.head:
			return False
		return True

	def __repr__(self):
		if self.is_empty():
			return "Waitlist Status: Empty"
		return_str = "Waitlist Status: "
		current = self.head
		while current is not None:
			return_str += str(current.data)
			if current.next:
				return_str += " -- "
			current = current.next
		return return_str

if __name__ == '__main__':
	stud1 = Student("Felicity", "Copenhaver")
	stud2 = Student("Kaili", "Wheeler")
	stud3 = Student("Robert", "Furr")

	waitlist = Queue()

	waitlist.add(stud1)
	waitlist.add(stud2)
	waitlist.add(stud3)

	while not waitlist.is_empty():
		print(waitlist)
		print("Size is: ", waitlist.size)
		waitlist.pop_left()
	print(waitlist)
