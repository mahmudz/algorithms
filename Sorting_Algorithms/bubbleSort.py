def bubbleSort(data, order):
	if order == 'asc':
		for i in range(len(data)):
			for j in range(i+1, len(data)):
				if data[i] > data[j]:
					data[i],data[j] = data[j],data[i]

	elif order == 'desc':
		for i in range(len(data)):
			for j in range(i+1, len(data)):
				if data[i] < data[j]:
					data[i],data[j] = data[j],data[i]

	return data


if __name__ == '__main__':
	data = [2,7,4,1,5]

	print('Sorting as ascending order')
	ASCsortedList = bubbleSort(data, 'asc')
	print(ASCsortedList)

	print('Sorting as descending order')
	DESCsortedList = bubbleSort(data, 'desc')
	print(DESCsortedList)