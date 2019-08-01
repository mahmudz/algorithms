def linearSearch(data, sItem):
	count = 0
	found = 0
	for i in range(len(data)):
		if sItem == data[i]:
			count += 1 
			found = 1

	if found == 1:
		print("Item Found. ")
		print(f"Total Appearance: {count}")
	else:
		print("Item Not Found.")


if __name__ == '__main__':
	
	data = [2,3,4,7,8,4,1,7,5,1,6,7,4,1,6,8,7,4,1,5]
	sItem = 50
	print(f"Searching For: {sItem}")

	linearSearch(data, sItem)