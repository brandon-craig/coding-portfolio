class Node:
	def __init__(self):
		self.value = None
		self.next = None

	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self, value):
		self.head = None
		self.tail = None

	def addNode(self, value):
		newNode = Node(value)

		if self.head == None:
			self.head = newNode

		if self.tail != None:
			self.tail.next = newNode

		self.tail = newNode

	def removeNode(self, index):
		head = self.head
		prevNode = None

		for i in range(0, index):
			if head != None:
				prevNode = head
				head = head.next
			else
				break

		if prevNode == None:
			self.head = head.next

		else:
			prevNode.next = head.next

	# Method to determine if a cycle exists in the singly linked list
	# A cycle has occurred when there is no node in the list that doesn't point to another node in the list. 
	def hasCycle(self):
		head = self.head

		if head == None or head.next == None:
			return False

		nodeOne = nodeTwo = head

		while nodeTwo != None and nodeTwo.next != None:
			nodeOne = nodeOne.next
			nodeTwo = nodeTwo.next.next

			if nodeOne == nodeTwo:
				return True

		return False
