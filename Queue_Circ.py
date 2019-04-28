class  ArrayQueue:
	"""FIFO queue implementation using a Python list as underlying storage """
	DEFAULT_CAPACITY = 10

	def __init__(self):
		""" Create an empty queue"""
		self._data = [None] * ArrayQueue.DEFAULT_CAPACITY #list with fixed Capcatity
		self._size = 0  #number of elements stored in the queue
		self._front = 0 #represents index of the first element of the queue in _data


	def __len__(self):
		""" Return the # of elements in the queue """
		return self._size

	def is_empty(self):
		"""Return True of the queue is empty"""
		return self._size == 0

	def first(self):
		""" Return (but do not remove) the element at the front of the queue
		Raise Empty Exception if Q is empty"""
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._data[self._front]

	def dequeue(self):
		"""Rmv & return the first element of queue FIFO"""
		if self.is_empty():
			raise Empty('Queue is empty')
		answer = self._data[self._front]
		self._data[self._front] = None   #help garbage collection
		self._front = (self._front + 1) %len(self._data)
		self._size -= 1
		if 0 < self._size < len(self._data) // 4:
			self._resize(len(self._data)//2)
		return answer

	def enqueue(self, e):
		"""Add an element to the back of the queue"""
		if self._size == len(self._data):
			self._resize(2 * len(self._data)) #double the array size
		avail = (self._front + self._size) % len(self._data)
		self._data[avail] = e
		self._size += 1

	def _resize(self, cap):             #assume cap >= len(self)
		"""Resize to a new list of capacity >= len(self)"""
		old = self._data                 #keep track of existing list
		self._data = [None] * cap        #allocate list with new capacity
		walk = self._front
		for k in range(self._size):      #only consider existing elements
			self._data[k] = old[walk]    #intentionally shift indices
			walk = (1 + walk) % len(old) #use old size as modulus
		self._front = 0                  #front has been aligned


















