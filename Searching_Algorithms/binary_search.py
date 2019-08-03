'''
	Filename: binary_search.py

	Algo Description: Binary search is a search algorithm that
	finds the position of a target value within a sorted array.
	Binary search compares the target value to the middle element of the array.
	
	Worst-case space complexity‎: ‎O(1)
	Worst-case performance‎: ‎O(log n)
	Best-case performance‎: ‎O(1)
	Average performance‎: ‎O(log n)

'''
from math import floor

def binarySearch(data, sItem):
	l = 0
	r = len(data) - 1

	while l <= r:
		m = floor((l + r) / 2)
		if data[m] < sItem:
			l = m + 1
		elif data[m] > sItem:
			r = m - 1
		else:
			print("Item Found. ")
			return

	print("Item Not Found.")


if __name__ == '__main__':
	data = [1,2,3,4,5,6,7,8,9]

	binarySearch(data, 9)
	binarySearch(data, 1)
	binarySearch(data, 5)
