def selectionSort(data, order):
	if order == 'asc':
		minIndex = 0
		for i in range(len(data) - 1):
			minIndex = i
			for j in range(i+1, len(data)):
				if data[j] > data[minIndex]:
					minIndex = j
				
				data[j],data[minIndex] = data[minIndex],data[j]

	elif order == 'desc':
		maxIndex = 0
		for i in range(len(data) - 1):
			maxIndex = i
			for j in range(i+1, len(data)):
				if data[j] < data[maxIndex]:
					maxIndex = j
				
				data[j],data[maxIndex] = data[maxIndex],data[j]

	return data


if __name__ == '__main__':
	data = [0,5,1,3,2,4,7,6,8,9]

	print('Sorting as ascending order')
	ASCsortedList = selectionSort(data, 'asc')
	print(ASCsortedList)

	print('Sorting as descending order')
	DESCsortedList = selectionSort(data, 'desc')
	print(DESCsortedList)