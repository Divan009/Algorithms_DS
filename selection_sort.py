def findSmallest(arr):
	smallest = arr[0]  #stores the smallest value
	smallest_index = 0  #stores the index of the smallest value
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

#sorts an array
def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		#finds the smallest element in array
		smallest = findSmallest(arr)
		#adds it to the new array
		newArr.append(arr.pop(smallest))
	return newArr

print(selectionSort([5,3,6,2,10]))