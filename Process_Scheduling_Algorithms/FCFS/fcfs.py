def findWaitingTime(ps):
	wt = [0] * len(ps)

	for i in range(1, len(ps)):
		wt[i] = ps[i - 1]['bt'] + wt[i-1]

	return wt


def findTurnArroundTime(ps,wt):
	tat = [0] * len(ps)

	for i in range(len(ps)):
		tat[i] = ps[i]['bt'] + wt[i]

	return tat

if __name__ == '__main__':
	ps = [
		{"name" : "P1", "bt" : 24},
		{"name" : "P1", "bt" : 3},
		{"name" : "P1", "bt" : 3}
	]

	wt = findWaitingTime(ps)
	tat = findTurnArroundTime(ps, wt)

	print('PS    BT    WT    TAT')
	print('----------------------')
	for i in range(len(ps)):
		print(f"{ps[i]['name']}    {ps[i]['bt']}     {wt[i]}    {tat[i]}")

	print(f'\nAverage Waiting Time: {sum(wt) / len(ps)}')
	print(f'Average TurnArround Time: {sum(tat) / len(ps)}')