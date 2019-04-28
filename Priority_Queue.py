class PriorityQueueBase:
	"""Abstract base class for a priority Queue"""

	class _Item:
		"""Lightweight composite to store priority queue items"""
		__slots__ = '_key', '_value'

		def __init__(self, k, v):
			self._key = k
			self._value = v

		def __It__(self, other):
			return self._key < other._key #compare items based on their key

	def isEmpty(self): #concrete method assuming Abstract len
	"""Return True if the priority Queue is isEmpty"""
		return len(self) == 0


######  Implementation using Unsorted List	
class UnsortedPriorityQueue(PriorityQueueBase): #base class defines _Item
	"""A min oriented PriorityQueue implemented with an unsorted array"""

	def _find_min(self):    #nonpublic utility
		"""Returns Position of Item with min key"""
		if self.isEmpty():   #isEmpty inherited from base class
			raise Empty('PriorityQueue is empty')
		small = self._data.first()
		walk = self._data.after(walk)
		while walk is not None:
			if walk.element() < small.element():
				small = walk
			walk = self._data.after(walk)
		return small

	def __init__(self):
		"""Create a new empty PriorityQueue"""
		self._data = PositionalList()

	def __len__(self):
		"""Return the number of items in PriorityQueue"""
		return len(self._data)

	def add(self, key, value):
		"""Add a key-value pair"""
		self._data.add_last(self._Item(key, value))

	def min(self):
		"""Return but dont rmv (k,v) with min_key"""
		p = self._find_min()
		item = p.element()
		return (item._key, item._value)

	def removeMin(self):
		"""remove and return (k,v) with min_key"""
		p = self._find_min()
		item = self._data.delete(p)
		return (item._key, item._value)

######  Implementation using sorted List	
class SortedPriorityQueue(PriorityQueueBase): #base class defines _Item
	"""A min oriented PriorityQueue implemented with a sorted list"""

	def __init__(self):
		"""Create a new empty PriorityQueue"""
		self._data = PositionalList()

	def __len__(self):
		"""Return the number of items in PriorityQueue"""
		return len(self._data)

	def add(self, key, value):
		"""Add a key-value pair"""
		newest = self._Item(key, value)  #make new item instance
		walk = self._data.last()  #walk backward looking for smaller key
		while walk is not None and newest < walk.element():
			walk = self._data.before(walk)
		if walk is None:
			self._data.add_first(newest)  #new key is smallest
		else:
			self._data.add_after(walk, newest) #newest goes after walk

	def min(self):
		"""Return but dont rmv (k,v) with min_key"""
		if self.isEmpty():   #isEmpty inherited from base class
			raise Empty('PriorityQueue is empty')
		p = self._data.first()
		item = p.element()
		return (item._key, item._value)

	def removeMin(self):
		"""remove and return (k,v) with min_key"""
		if self.isEmpty():   #isEmpty inherited from base class
			raise Empty('PriorityQueue is empty')
		item = self._data.delete(self._data.first())
		return (item._key, item._value)

